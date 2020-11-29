# Simple calculations to find RMSE for train and test variables and then calculate percent change from base
# Note: mse has been abbreviated from sklearn

def rmse_report(X_train, X_test, y_train, model):
    y_hat_train = model.predict(X_train)
    rmse_train = mse(y_train, y_hat_train)**0.5
    y_hat_test = model.predict(X_test)
    rmse_test = mse(y_test, y_hat_test)**0.5
    rmse_vanilla = 177703.18334308316
    print(f'Train RMSE: {rmse_train} \n Test RMSE: {rmse_test}')
    print('Percent change: ', round(((rmse_test-rmse_train)/rmse_train)*100, 3))
    print('Percent change (Base Model vs. Updated Model): ', round(((rmse_train-rmse_vanilla)/rmse_vanilla)*100, 3))