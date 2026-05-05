# Final Project for IS 477: Fuel the Data



# Title

## Contributors

## Summary
Crime rates in the United States vary considerably from state to state, and these differences are widely believed to reflect underlying socioeconomic conditions. While crime is shaped by many factors—historical, cultural, institutional—poverty, unemployment, and income inequality are commonly cited as structural drivers. This project investigates how these socioeconomic indicators relate to crime levels across U.S. states, with the goal of identifying which factors are most strongly associated with higher crime.

We integrate three publicly available datasets: crime statistics from the FBI's Uniform Crime Reporting (UCR) program (2024), poverty estimates from the USDA Economic Research Service (2023), and unemployment rates and median household income from the same USDA ERS data product (2022–2023). Because each dataset reports values at the state level (or can be aggregated to the state level), they can be merged on state name and analyzed jointly.

Our research questions are:

-	RQ1: How are poverty rates related to crime rates across U.S. states?
-	RQ2: Is unemployment associated with higher crime levels?
-	RQ3: How does median household income relate to variations in crime rates across states?
-	RQ4: Which socioeconomic indicators appear to be the strongest predictors of crime levels?

After cleaning and merging the three datasets into a unified state-level dataset, we performed exploratory data analysis using scatter plots, correlation analysis, and linear regression. Key findings:

-	Poverty rate showed only a weak relationship with crime variables (correlations ranging from 0.04 to 0.19), suggesting that poverty alone does not strongly explain variation in state-level crime.
-	Unemployment rate showed a moderate positive correlation with violent and property crime (around 0.44–0.49). Linear regression confirmed unemployment as a meaningful predictor (positive coefficient ≈ 16,799 for violent crime).
-	Median household income showed a very weak relationship with violent crime (r ≈ 0.17), again indicating that income alone is not a strong predictor.
-	Comparing all three predictors, unemployment rate emerged as the strongest socioeconomic correlate of crime; in a multiple regression including all three variables, unemployment remained the dominant predictor.

We also observed that crime variables themselves are highly intercorrelated (r > 0.9), meaning states with high levels of one type of crime tend to have high levels of others. This pattern likely reflects differences in state population size as much as differences in per-capita crime, and it is a limitation that future work should address through normalization.

Overall, the analysis suggests that unemployment is a more consistent socioeconomic correlate of crime than either poverty or income, but that the explanatory power of these variables individually is modest. This points to the need for additional factors—such as education, urbanization, population density, and demographic composition—to fully understand state-level crime variation.

## Data Profile

### Dataset 1 — FBI Uniform Crime Reporting (UCR), 2024
Source: FBI Crime Data Explorer, "Offenses Known to Law Enforcement by State by City, 2024" (CIUS Table 8) URL: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads Location in repository: data/offenses-known-to-le-2024/CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx Format: Excel (.xlsx)

This dataset contains counts of reported offenses by city within each state. Variables used in this analysis: State, Violent crime, Murder and nonnegligent manslaughter, Rape, Robbery, Aggravated assault, Property crime, Burglary, Larceny-theft, and Motor vehicle theft. Because the dataset is reported at the city level, we aggregated all cities within each state using groupby('State').sum() to produce state-level totals.

The UCR program is voluntary and not all law enforcement agencies report consistently. As a result, crime counts may underrepresent true offense levels in states with lower reporting rates. Aggregate crime statistics can also reflect differences in policing and reporting practices rather than actual differences in criminal behavior.

Ethical and legal constraints: UCR data are public domain (U.S. federal government work, 17 U.S.C. § 105). No personally identifiable information is included. The FBI explicitly cautions against using UCR data to rank or compare locations.

Relation to research questions: Provides the dependent variables (crime counts by type) for all four research questions.

### Dataset 2 — USDA ERS Poverty Estimates, 2023
Source: U.S. Census Bureau Small Area Income and Poverty Estimates (SAIPE), accessed via USDA Economic Research Service URL: https://ers.usda.gov/data-products/county-level-data-sets Location in repository: data/PovertyReport.xlsx Format: Excel (.xlsx)

State-level poverty estimates for 2023, including the percentage of all people in poverty and the percentage of children in poverty, with 90% confidence intervals. The dataset covers all 50 states, the District of Columbia, and a national aggregate row (excluded from analysis). Variables used: Name (state) and Percent (overall poverty rate, 2023).

The data are model-based estimates produced by the SAIPE program using administrative records and survey data, so they carry statistical uncertainty as reflected in the confidence intervals.

Ethical and legal constraints: Public domain U.S. government data with no redistribution restrictions.

Relation to research questions: Independent variable for RQ1 and contributes to RQ4.

### Dataset 3 — USDA ERS Unemployment and Median Household Income
Source: Bureau of Labor Statistics LAUS program (unemployment) and Census Bureau SAIPE (income), accessed via USDA ERS URL: https://ers.usda.gov/data-products/county-level-data-sets Location in repository: data/UnemploymentReport.xlsx Format: Excel (.xlsx)

State-level annual unemployment rates from 2015 through 2023 and median household income for 2022. Covers all 50 states, the District of Columbia, and Puerto Rico (excluded from merged analysis because it is not present in the crime or poverty datasets). Variables used: Name (state), 2023 unemployment rate, Median Household Income (2022).

Ethical and legal constraints: Public domain U.S. government data.

Relation to research questions: Provides the independent variables for RQ2 (unemployment) and RQ3 (income), and contributes to RQ4.
Integration
All three datasets share state name as a common key. The crime dataset's state names were converted to title case (.str.title()) to match the format used in the poverty and unemployment datasets, and inner joins on State were used to retain only states present in all three sources. The resulting merged dataset contains one row per state with poverty rate, unemployment rate, median household income, and crime counts as variables.

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

Several directions could meaningfully extend this analysis.

Normalize crime by population. The single most important next step is to convert raw crime counts to per-capita rates (e.g., crimes per 100,000 residents). Large-population states naturally have larger absolute crime counts, and this confounds correlations between socioeconomic variables and crime. Using rates rather than counts would isolate genuine differences in crime intensity from differences in state size. We have prepared the data structure to support this; we simply need to merge in state population estimates and divide.

Add socioeconomic variables. The three predictors we examined—poverty, unemployment, income—are commonly cited but far from exhaustive. Education attainment (for example, the percentage of adults with a bachelor's degree), urbanization, income inequality (Gini coefficient), age structure, and racial/ethnic composition have all been linked to crime in prior research. Including these would substantially improve model explanatory power and yield a more nuanced picture of which factors matter.

Move from cross-sectional to longitudinal. The unemployment dataset already includes annual values from 2015 through 2023. Combining this with multiple years of UCR data would enable panel-data analysis—asking whether changes in unemployment within a state predict changes in crime in subsequent years, rather than only comparing across states at a single point in time. This kind of analysis is much closer to causal inference than cross-sectional correlation.

Move to county or city level. State-level analysis hides substantial within-state variation. The USDA ERS datasets are available at the county level, and the FBI UCR data are at the agency level (which can be aggregated to county). Running the analysis at a finer geographic resolution would dramatically increase the sample size (from ~50 states to thousands of counties) and reveal patterns invisible at the state level.

More rigorous statistical methods. Beyond simple linear regression, we could apply spatial regression (to account for geographic autocorrelation between neighboring states), regularized regression like LASSO (to handle multicollinearity among predictors), or hierarchical models (to account for variation across regions). Each of these would address specific limitations of the basic OLS regression we used.

Account for reporting differences. UCR data depend on voluntary law enforcement reporting and may underrepresent crime in agencies with lower participation rates. Cross-referencing with the Bureau of Justice Statistics' National Crime Victimization Survey would help triangulate the true crime burden, especially for crimes that are likely underreported.

Lessons learned. Working through this project taught us that data cleaning is rarely a single step but a sequence of small, specific fixes that each address a distinct quality issue. We also learned that the choice of analytic unit matters enormously: aggregating city-level crime data to the state level was necessary for integration but introduced the population-confounding issue that limits the strength of our conclusions. Finally, we learned that the first round of analysis is rarely the final word — patterns observed at the state level open up further questions about why those patterns exist and what they would look like at finer scales.

## Challenges
We encountered several substantive challenges during the project, which shaped both the workflow and our final approach.

Excel file structure. The raw Excel files from FBI UCR and USDA ERS were not clean tabular data — they included headers, footnote rows, multi-row column labels, and explanation text intended for human readers. We could not load them directly with pd.read_excel(...) because the parser would treat the header rows as data. We used the skiprows parameter to skip the metadata rows and locate where the actual table started, which required manual inspection of each file.

Column naming inconsistencies. The crime dataset's column names included embedded newline characters (e.g., Murder and\nnonnegligent\nmanslaughter) and surrounding whitespace, which made them difficult to reference in code. Standard string operations (str.replace('\n', ' ') followed by .str.strip()) resolved this but only after we identified the issue through exploratory printing of crime.columns.

Mismatched analysis units. This was the most consequential challenge. The crime data are reported at the city level (multiple rows per state), while the poverty and unemployment data are at the state level. Direct merging would have produced a many-to-one mismatch. We solved this by aggregating crime data to the state level via groupby('State').sum().reset_index(), but this aggregation introduces the issue that crime totals reflect both crime intensity and state population — a limitation that affects all of our findings.

State name format mismatch. The crime dataset's State column was uppercase (e.g., "ALABAMA"), while the other two datasets were title case ("Alabama"). Without standardization the merge would have produced no matches at all. Applying .str.title() resolved this.

Currency formatting in income column. Median household income was stored as text with a dollar sign and comma (e.g., "$59,703"). We had to strip these characters before converting to numeric, otherwise the column would have remained as strings and could not be used in regression analysis.

Temporal alignment. Crime data are from 2024, poverty from 2023, income from 2022. We treated these as approximately contemporaneous because state-level socioeconomic structure changes slowly, but this is a real limitation we would address in follow-up work by aligning to a single reference year.

Small sample size. Our final dataset has only 50 observations (states + DC). Correlation and regression estimates based on n ≈ 51 carry substantial uncertainty, and small-sample effects can drive what look like meaningful relationships. We chose to report correlations as descriptive statistics rather than as hypothesis tests for this reason.

These challenges all map back to the data-cleaning operations described above; each cleaning step is a response to a specific challenge we encountered during data profiling.

## Reproducing

To reproduce this analysis from scratch:

1.	Clone the repository:

git clone https://github.com/soobinj2/fuelthedata.git

cd fuelthedata

2.	Install Python dependencies:

pip install -r requirements.txt

3.	Verify the input data files. The data/ directory should contain:

-	data/PovertyReport.xlsx
-	data/UnemploymentReport.xlsx
-	data/offenses-known-to-le-2024/CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx

These files are committed to the repository. If you need to re-acquire them from the original sources, see scripts/download_data.py for documentation of the manual download steps (the source websites do not provide direct download URLs).

4.	Verify data integrity:

python scripts/download_data.py

This script computes SHA-256 hashes of each input file and compares them against the values recorded in checksums.txt. All three files should report [PASS].

5.	Run the data integration script to produce the merged dataset:

python scripts/clean_and_merge.py

This produces results/merged_data.csv.

6.	Run the analysis notebook:

jupyter notebook data_analysis/dataanalysis_1.ipynb

Run all cells (Kernel → Restart & Run All) to reproduce all visualizations and statistical outputs. The pre-computed visualization outputs are also stored in results/figures/.

## References
