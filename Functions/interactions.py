def find_interactions(n, model, ind_train):
    """
    Returns n most predictive interactions based on low MSE.
    
    Parameters:
    n: int. the number of interactions selected.
    model: LinearRegression() object being tested. 
    ind_train: the independent variables in the training set.
    """
    # create a combination of all possible pairs of explanatory variables
    combos = list(combinations(ind_train.columns, 2))
    print('Testing {} combinations.\n'.format(len(combos)))
    inters = [(0,0,0)]*n
    # X variable for testing set equal to the inputed dataset
    temp_X = ind_train.loc[:]
    
    # Loop through every pair
    for combo in combos:
        # Create the interaction via multiplication
        temp_X['interaction']=(ind_train.loc[:, combo[0]]
                               *ind_train.loc[:, combo[1]])
        # Run linear regression on this new intercation
        linreg = LinearRegression()
        model = linreg.fit(temp_X, y_train)
        y_pred = model.predict(temp_X)
        score = round(r2_score(y_train, y_pred),3)
        # If sthe score was better than the last one, throw it in there
        if score > inters[-1][0]:
            # Note, these are just the pairs we are appending. We will have to add this to the model separately
            inters.append((score, combo[0], combo[1]))
            inters = sorted(inters, reverse=True)[:n]
    for inter in inters:
        # inter 1 is first var in combo, inter 2 is the second var, inter 0 is the new interaction
        print('R^2 including interaction of {} and {}: {}'
              .format(inter[1], inter[2], inter[0]))
        #plot_interaction(inter[1], inter[2])
    # creating a list of interactions
    fin_inters = [i[1:] for i in inters]
    return fin_inters