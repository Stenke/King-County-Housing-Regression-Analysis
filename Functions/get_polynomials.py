def get_polynomial_features(ind_train, 
                            max_degree = 3):
    """
    Returns the best fit polynomial degree for each variable in ind_train.
    
    Parameters:
    ind_train: DataFrame of training variables
    max_degree: the maximum degree tested for polynomial factor selection
    
    """
    features = []
    for col in ind_train.columns:
        scores = []
        for degree in range(1,max_degree + 1):
            df = pd.DataFrame(ind_train[col])
            # Run polynomial fit for each degree for each column
            poly = PolynomialFeatures(degree)
            X_poly_train = poly.fit_transform(df)
            reg_poly = LinearRegression().fit(X_poly_train,
                                              y_train)
            # See how the new polynomial performs - scored based on MSE
            y_pred = reg_poly.predict(X_poly_train)
            score = round(mse(y_train, y_pred),5)
            scores.append((score, degree, col, df, y_pred))
            # Take best score from list of scores (stored as tuples) - not reversed because lower is better
            best_score = sorted(scores)[0] 
        # See if the degree of the best score is greater than 1, if so, add the new coloumn and degree
        if best_score[1] > 1:
#             print('Factor {} by {}. R^2: {}'
#                   .format(best_score[2], 
#                           best_score[1], best_score[0]))
#             plt.scatter(best_score[3], y_train, alpha = .1)
#             plt.scatter(best_score[3], best_score[4], 
#                         c='red', label=('Predicted Values'))
#             plt.legend()
#             plt.show()
            features.append((best_score[2], best_score[1]))
    return features 