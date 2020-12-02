def report(model, ind_train, ind_test, save_as = None):
    """
    Print relevant statistics for a model.
    
    Parameters:
    model: Fitted LinearRegression object
    ind_train: independent variables for training set
    ind_test: independent variables for test set
    """
    pred_y_train = model.predict(ind_train)
    pred_y_test = model.predict(ind_test)
    
    #Print top and bottome variables by size of coefficient.
    coefs = []
    high_coefs = []
    low_coefs = []
    for i in range(0, len(model.coef_)):
        coefs.append((model.coef_[i],ind_train.columns[i]))
    for coef in coefs:
        if ((coef[0] 
            < np.quantile(model.coef_,.05))
            or (coef[0] 
            > np.quantile(model.coef_,.95))):
            high_coefs.append(coef)
    for coef in coefs:
        if ((coef[0] 
            < .01)
            and (coef[0] 
            > -.01)):
            low_coefs.append(coef)
    print('************\nHigh Impact Variables:\n')
    for variable in high_coefs:
        print('Variable: {}\nCoefficient: {}\n'
              .format(variable[1],variable[0]))
 

    #Print R^2 against the test data. 
    print('Train R^2: {}'
          .format((r2_score(y_train,pred_y_train))))
    print('CrossValidated R^2: {}'
          .format(np.mean(cross_val_score(model,
                                          ind_train, y_train, 
                                          scoring ='r2', 
                                          cv = crossval))))
    print('Test R^2: {}\n'
          .format(r2_score(y_test,pred_y_test)))
    

    plotdf = pd.DataFrame([])
    plotdf['test_resids'] = pred_y_test-y_test
    plotdf['y_test'] = y_test
    

    
    plt.scatter(pred_y_test, y_test, alpha=.10, c='deepskyblue')
    plt.plot(pred_y_test, pred_y_test, c='gold', 
             label='Predicted Price')
    plt.xlabel('Predicted Price')
    plt.ylabel('Actual Price')
    plt.legend()
    plt.title('Residuals Against Test Set')
    if save_as != None:
        plt.savefig(save_as);