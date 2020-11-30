# Seattle-Housing-Regression-Analysis
A predictive model for housing prices in King County, Washington using multiple regression.

# Business Problem
We are a new real estage agency, Rest, with a customer-friendly realtors paired with an online site for price prediction. Initially, we are only operating in King County. In order to both attract customers online and to help our realtors tailor specific needs to our home buyers and sellers, we need a prediction model that will accurately predict home prices after features are uploaded.

Our prediction model will both help online users find out the price of their specific home or to look at potential prices of homes with certain features in specific locations.

For our initial roll-out, Rest is focusing on mid-range houses priced $200,000 to $790,000

# The Data
This project uses the King County House Sales dataset, which can be found in kc_house_data.csv in the data folder in this repo. The description of the column names can be found in column_names.md in the same folder.

Additionally, you will find a cleaned data set where features are added and our final modeling data.

## Questions
The following questions will guide our analysis and modeling as we look for opportunities for our business.

1. What price range are catering towards?

2. Are there specific locations where we should focus?

3. What features are most important for predicting home prices?

4. Any additional opportunities uncovered in the analysis?


## Methods
Data obtained from King Country housing dataset. Data was scrubbed and cleaned to remove outliers and null values. Null values were filled either with 0's or the median values depending on the situation. Additionally, we binned certain features like bathrooms to reduce inputs and transformed other features into binary columns like renovated (either yes or no instead of years renovated). We then looked at a scatter matrix to get an idea of which explanatory variables may be useful.

![Scatter-Matrix](https://github.com/Stenke/Seattle-Housing-Regression-Analysis/blob/main/Figures/Scatter-Matrix.png "EDA-Scatter-Matrix")

For our various models, dummy variables were created for categorical data. We also replaced zipcodes with their respective cities in King County. In order to meet assumptions for our models, we removed outliers by limiting pricing data to 2 standard deviations (95%).

After assuring regression assumptions, we used Scikit-Learn and Statsmodels libraries to create a baseline model for predicting housing prices. Using train-test-split, we iterated on the model to remove collinearity, extraneous variables, and created features all while aiming for an improved R-squared value and reduced RMSE. QQ plots were used to determine normality in our models. Finally, we performed cross-validation to ensure our model meets our expecation for generalization.

## Findings
Our final model process consisted of the following:

1. Vanilla Model

2. Model 2: Pricing Outliers Removed

3. Model 3: Scaled Explantory Variables (Min/Max)

4. Model 4: Find & Add Interactions

5. Model 5: Polynomial Variables Added

6. Model 6: P-Value Filtered (Stepwise Function)

Our final model has an Adjusted R-Squared of 0.760 meaning 76% of the variability in house pricing (dependent variable) can be explained by our explantory variables in our model. Additionally, we reduced the root-mean-squared-error to 77,710, a 56.52% improvement. This means we can more accurately predict the housing price with less error on either end. The test prediction model was within 1.10% of the training model. Additionally, our cross-validated R-Squared is only 1.0% different from our training model. This is shows that the generalization of our model in the wild is promising. Of course, we'll never know until we try it!


## Conclusion
We are focusing on homes in the $200,000 - $790,000 price range initially. This is both what our model is best suited for and aligns with opportunities we see in the data. Using the most impactful variables based on coefficients, we found specific opportunities especially based on cities. After looking at additional data provided by King County, we noticed that house pricing seemed to correlate with kindergarten readiness and enrollment. We suspect this extends to other school metrics.

With this in mind, we feel especially equipped for helping young families with well-paying jobs find their first home in Seattle and its suburbs. We found opportunities for customers who are looking for housing in a great school district for younger children that is still affordable. One example of this is Lake Washington School District, which includes the neighboring cities of Kirkland and Redmond. In our model, we see that Kirkland has a large positive coefficient, which is to be expected as it is known to be a wealthy suburb of Seattle. Right next door is Redmond that our model found a negative impact on pricing, meaning we can find affordable housing in a great school district and close access to similar ammenities. At Rest, we feel especially equipped for finding these opportunities for our young and aspiring families.
