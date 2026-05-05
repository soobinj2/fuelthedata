# Final Project for IS 477: Fuel the Data



# Title

## Contributors

## Summary

## Data Profile

## Data Quality

We conducted several checks to assess the quality and reliability of the dataset before performing analysis.

First, we verified the presence of missing values using `.isnull().sum()`. The results showed that there were no missing values across all variables, indicating that the dataset is complete and does not require imputation.

Next, we examined summary statistics using `.describe()` to understand the distribution, range, and variability of each variable. This allowed us to identify differences in scale across variables, as well as potential anomalies.

We also visualized the distribution of key variables using histograms. For example, the poverty rate distribution appeared relatively concentrated within a specific range, suggesting consistency across states.

To further assess data quality, we used boxplots to detect potential outliers in crime-related variables. The boxplot for violent crime revealed several extreme values. These outliers likely represent real-world variations between states rather than data errors, so they were retained for analysis.

Additionally, correlation analysis was performed to understand relationships between variables. While this is primarily used for analysis, it also helped confirm that variables behave as expected (e.g., crime variables being highly correlated with each other).

Overall, the dataset is clean, complete, and suitable for analysis, with some natural variability and outliers that reflect real-world differences rather than data quality issues.


## Data Cleaning

The datasets required multiple preprocessing steps to ensure consistency and usability for analysis.

First, we selected only the relevant columns from each dataset. For example, from the poverty dataset, we extracted the "Name" and "Percent" columns and renamed them to "State" and "Poverty Rate" for clarity. Similarly, from the unemployment dataset, we selected the 2023 unemployment rate and standardized the column names.

The crime dataset required additional cleaning due to formatting inconsistencies. Column names contained newline characters and extra spaces, which were removed using string replacement and trimming functions. This ensured consistent column naming across the dataset.

Since the crime data was originally at the city level, we aggregated it to the state level using `groupby("State").sum()`. This step was necessary to align it with the poverty and unemployment datasets, which are already at the state level.

We also standardized the "State" column across all datasets to ensure consistent formatting (e.g., capitalization), enabling accurate merging.

After cleaning each dataset individually, we merged them into a single dataset using the "State" column as the key. This resulted in a unified dataset containing socioeconomic and crime variables for each state.

Finally, we verified the merged dataset by checking its shape and previewing the data to ensure that all variables were correctly aligned and no unintended data loss occurred.

These cleaning steps ensured that the final dataset was structured, consistent, and ready for analysis.


## Findings

### RQ1: How are poverty rates related to crime rates across U.S. states?

Through this section, we analyzed the relationship between poverty rate and crime variables. Scatter plots between poverty rate and different types of crime (violent crime, robbery, aggravated assault, and burglary) show widely dispersed data points with no clear linear pattern. 

Also, correlation analysis shows that the poverty rate has a weak relationship with crime variables, with correlation values ranging from 0.04 to 0.19. This supports that there is no strong or consistent association between poverty levels and crime rates across states. 

Overall, the results suggest that poverty alone is not a significant factor in explaning variations in crime.

### RQ2: Is unemployment associated with higher crime levels?

Unemployment rate shows a moderate positive relationship with violent crime. The regression plot shows a clear upward trend, and the correlation coefficient(approximately 0.46) supports this observation.

Additional comparisions across different crime categories also show consistent positive trends, suggesting that higher unemployment is a meaningful factor in explaining crime variation across states. 

In addition to correlation analysis, linear regression was performed to further examine the relationship between unemployment and violent crime. The regresson results show a strong positive coefficient for unemployment rate (approximately 16,799), incresed in unemployment is associated with a substantial increase in violent crime.

When controlling for poverty rate in a multiple regression model, unemployment remains the dominant predictor with a significantly larger coefficient, while poverty shows minimal impact. This further reinforces the conclusion that unemployment is a key factor influencing crime rates.


### RQ3: How does median household income relate to variations in crime rates across states?

The analysis reveals a very weak relationship between median household income and violent crime. The scatter plot shows no clear pattern, and the regression line is nearly flat. The correlation coefficient (= 0.17) further confirms that the association is minimal.

This suggests that income alone is not a strong predictor of crime rates across states.


### RQ4: Which socioeconomic indicators appear to be the strongest predictors of crime levels?

Comparing all variables, unemployment rate emerges as the strongest predictor of crime among the socioeconomic factors considered.

Correlation analysis shows that unemployment has the highest association with violent crime (= 0.46), while median income (= 0.17) and poverty rate (= 0.11) show much weaker relationships. 

Regression analysis further supports this finding, as unemployment rate has the largest coefficient, indicating a stronger influence on crime levels.

Overall, these results suggest that unemployment plays a more significant role in explaining variations in crime across states compared to poverty or income.






## Future Work

## Challenges

## Reproducing

## References
