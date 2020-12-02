
def add_interactions(interactions, ind_train, ind_test):
    """
    Use forward selection based on lowest MSE to select
    and add most predictive interactions to a new model.
    
    Parameters:
    interactions: list of tuples outputed by find_interaction
    function.
    ind_train: independent variables training data.
    ind_test: independent variables test data.
    
    Returns:
    (new_model, new_x_with_interactions)
    """
    additions = interactions
    X_temp_tr = ind_train.loc[:]
    X_best_tr = ind_train.loc[:]
    X_best_t = ind_test.loc[:]
    scores = []
    baseline = 0
    # Additions = True, so will run through the length of them
    while additions:
        # Inter is the list of each combo of variables found using find_interactions
        for inter in additions:
            # Create a new column with the name of each variable in the tuple & do the actual multiplaction of these vars
            X_temp_tr[inter[0]
                      +' * '
                      +inter[1]]=(X_temp_tr.loc[:, inter[0]]
                                  *X_temp_tr.loc[:, inter[1]])
            # After creating the interaction and new column for all rows, run lin reg to test it
            linreg = LinearRegression()
            model = linreg.fit(X_temp_tr, y_train)
            y_pred = model.predict(X_temp_tr)
            score = round(r2_score(y_train, y_pred),5)
            scores.append((score, inter[0], inter[1]))
            # Take the highest score and set to best
            best = sorted(scores, reverse=True)[0]
            X_temp_tr = X_best_tr.loc[:]
        scores = []
        if best[0] >= baseline:
            # Remove selected best combo from list
            additions.remove(best[1:])
            # New baseline was previous beset score
            baseline = best[0]
            # Create interactions for train and test variables
            X_best_tr[best[1]
                      +' * '
                      +best[2]]=(X_temp_tr.loc[:, best[1]]
                                 * X_temp_tr
                                 .loc[:, best[2]])
            X_best_t[best[1]
                     +' * '
                     +best[2]]=(X_best_t.loc[:, best[1]]
                                *X_best_t.loc[:, best[2]])
            X[best[1]
              +' * '
              +best[2]]=(X.loc[:, best[1]]
                         *X.loc[:, best[2]])
            linreg = LinearRegression()
            model = linreg.fit(X_best_tr, y_train)
            y_pred = model.predict(X_best_tr)
            t_pred = model.predict(X_best_t)
            print('Interaction Added: {} * {}'
                  .format(best[1], best[2]))
        else:
            print('complete')
            break
    linreg = LinearRegression()
    new_model = sm.OLS(y_train, X_best_tr).fit()
    
    return(new_model, X_best_tr, X_best_t)