# Milestone 3: Status Report
## Group: Fuel the Data


## 1. Project Overview


This project is about the poverty rate, the unemployment rate and the crime rate in the United States. The project is trying to understand how the poverty rate and the unemployment rate affect the crime rate. The project is also looking at how the relationship between the poverty rate the unemployment rate and the crime rate's different for different types of crimes. In addition, this project aims to explore whether different types of crimes are influenced differently by socioeconomic factors. By examining multiple crime categories such as violent crime, robbery, aggravated assault, and burglary, the analysis seeks to provide a more detailed understanding of crime patterns across states. This approach allows us to go beyond a single overall crime metric and identify more specific relationships. Overall, This project focuses on identifying patterns across different states rather than analyzing individual cases. By using state-level data, the analysis provides a broader perspective on how socioeconomic conditions are related to crime trends in the United States.


## 2. Progress on Project 

- Collected the poverty rate data, the unemployment rate data and the crime data
- Cleaned up the Excel files by getting rid of headers and rows
- Used 'skiprows' to get only the data we needed from the Excel files
- Organized the column names in the Excel files so they all match
- Combined the poverty rate data and the unemployment rate data by state
- Aggregated city-level crime data to the state level
- Merged the crime data with the data, including the different types of crimes
- Made a scatter plot to visualize the data
- Correlation analysis to see how the data is related
- Performed additional comparisons across different crime categories to identify patterns
- Reviewed results and refined analysis based on observed patterns


## 3. Updated Timeline


| Task | Status | Expected Completion |
|------|--------|-------------------|
| Data Collection | Completed | Done |
| Data Cleaning | Completed | Done |
| Data Integration | Completed | Done |
| Exploratory Data Analysis | Completed | Done |
| Advanced Analysis | In Progress | Next Phase |
| Final Report Writing | Not Started | End of Project |




## 4. Changes to Project Plan

Our original plan was to use the crime data as it was. The poverty rate and unemployment rate data was given to us by state. This caused a problem because the crime data was by city. To fix this problem we decided to combine the crime data by state. This way all the data is consistent. We can compare and analyze it. We also wanted to look at more than the total crime numbers. We wanted to look at the types of crimes like robbery, assault and burglary. This change allowed us to improve the consistency of the dataset and ensured that all variables could be directly compared within the same level of analysis.


## 5. Challenges and Solutions

First, the data from the Excel file could not be used directly. This is because the Excel data file had a lot of headers and explanation rows that we did not need. To fix this issue we had to clean up the data by finding where the actual data started. We used the 'skiprows' option to do this.
Second, we had a problem with the column name. It had a line character in it which made it hard to access the data. The column name had something like \nData access was difficult because it included in it. We were able to fix this by using 'str.replace()' to organize the column name.
Third, merging the data was not easy. The reason is that the column names and formats were different, in each dataset. To solve this problem we had to make all the column names the same and convert the state name format to be consistent.
Fourth, the crime data was given to us in city units. This made it impossible to merge with data directly. To fix this issue we had to combine the crime data by state and make sure it matched the analysis unit as the other data. We did this by aggregating the crime data based on the state. The crime data was then matched to the analysis unit as the other data, which was also based on the state. Through these steps, we were able to improve the overall quality and reliability of the dataset.

## 6. Analysis Summary

The analysis showed that the poverty rate and the unemployment rate are somewhat related. The poverty rate and the crime rate are not very related.
The unemployment rate and the crime rate are more related. This means that the unemployment rate might have an effect on the crime rate.
The different types of crimes are very related. If one type of crime is high in a state the other types of crimes might also be high.
The scatter plot showed that it is hard to explain the crime rate with one variable. The data points are over the place. Some states have high crime rates, which means there might be other factors, at play.
These results suggest that unemployment may be a more important factor than poverty in explaining variations in crime across states.
In addition, when comparing different types of crimes, violent crime and aggravated assault appeared to show slightly stronger patterns with unemployment compared to other crime types. This suggests that certain types of crimes may be more sensitive to economic conditions than others.
Furthermore, the correlation analysis showed that different crime variables are highly correlated with each other. This indicates that states with high levels of one type of crime tend to also have high levels of other crimes, suggesting an overall pattern of crime concentration.
These findings imply that crime is influenced by multiple factors and cannot be explained by a single variable such as poverty alone. Economic instability, particularly unemployment, may play a more important role in explaining variations in crime across states.
Overall, this analysis highlights the importance of considering multiple socioeconomic factors when studying crime patterns. While poverty alone does not strongly explain crime rates, unemployment shows a more consistent relationship, suggesting that economic instability may play a key role in influencing crime. These findings provide a foundation for future work that could incorporate additional variables or more advanced analytical methods. These results also suggest that the relationship between socioeconomic factors and crime is complex and may vary depending on the type of crime being analyzed. Therefore, further analysis with additional variables could provide a more complete understanding of crime patterns.


## 7. Team member Contributions

- Soobin Jang
    - Data cleaning and processing for poverty and unemployment rates
    - Data merging and correlation analysis
    - EDA and interpretation of results

- Jiseok Han
    - Collection and cleaning of crime data
    - Assistance with data aggregation and merging
    - Support for reviewing and interpreting analysis results

## 8. Repository Artifacts

1. Data file: 'data/'
2. Data Analysis: 'data_analysis/dataanalysis_1'
3. Main Report: 'StatusReport.md'
