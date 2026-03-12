# Project Plan

## Overview

The goal of this project is to analyze the relationship between crime rates and socioeconomic factors in the United States. In the United States, crime rates vary greatly from region to region, and these differences are likely to be related to socioeconomic factors such as poverty rate, unemployment rate, and income level. Therefore, in this project, we will combine crime statistics and socioeconomic indicator data to examine how these factors relate to crime levels.

To this end, crime data provided by the FBI's Uniform Crime Reporting (UCR) program and socioeconomic indicator data provided by the USDA Economic Research Service will be used together. Socioeconomic data includes variables such as poverty rate, unemployment rate, and household median income. Since the two datasets commonly contain state-level information in the United States, the data can be combined based on this.

After collecting and organizing data, exploratory data analysis (EDA) will be performed to look at patterns between crime rates and socioeconomic variables. In addition, it plans to compare the level of crime by state and the distribution of socioeconomic indicators through various visualizations. If necessary, a simple statistical analysis or regression analysis will be used to further analyze how socioeconomic factors relate to crime rates.

The purpose of this project is to understand how the socioeconomic environment relates to crime patterns in the United States.


## Team

Soobin Jang
-Data Collection and preprocessing
-Data Cleaning and Merging

Jiseok Han
- Visualization and Statistical Analysis
- Documentation Support
- Writing and project presentation preperation

## Timeline

**Week 1 – Data Collection and Initial Review**

- Collect crime data from the FBI Uniform Crime Reporting (UCR) program

- Collecting socioeconomic indicator data (poverty rate, unemployment rate, household median income, etc.) from the USDA Economic Research Service

- Review the structure of each dataset and identify key variables for analysis

**Week 2 – Organize and preprocess data**

- Clean up data, such as removing unnecessary heat and checking missing values

- State identifiers and variable formats to combine two datasets

- Pre-processing for data consolidation

**Week 3 – Data Consolidation and Exploratory Data Analysis (EDA)**

- Combine crime data with socioeconomic data based on state unit identifiers

- Exploratory data analysis determines the distribution and summary statistics of variables

- Exploring the Early Patterns between Crime Rate and Socioeconomic Variables

**Week 4 – Visualization and Statistical Analysis**

- Create different visualizations comparing state-specific crime rates and socioeconomic indicators

- Exploring the correlation between poverty rate, unemployment rate, income level and crime rate

- Perform basic statistical analyses, such as correlation or regression, if necessary

**Week 5 – Interpretation of results and project completion**

- Interpret analysis results and summarize key findings

- Discuss the limitations of data and the meaning of analysis results


## Research Questions

RQ1: How are poverty rates related to crime rates across U.S. states?

RQ2: Is unemployment associated with higher crime levels?

RQ3: How does median household income relate to variations in crime rates across states?

RQ4: Which socioeconomic indicators appear to be the strongest predictors of crime levels?


## Datasets

- Dataset 1
FBI Uniform Crime Reporting (UCR) – Offenses Known to Law Enforcement (https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads)

 This dataset is official crime statistics collected by the FBI and contains information on the number of crimes committed by state and the type of crime. This allows you to compare crime patterns in each state in the United States.

- Dataset 2
USDA Economic Research Service – Socioeconomic Indicators (https://ers.usda.gov/data-products/county-level-data-sets)

 This dataset is socioeconomic indicator data provided by the US Department of Agriculture's Bureau of Economic Research and includes information such as poverty rate, unemployment rate, and household median income. The data can be used to identify differences in economic conditions between regions.

- How to integrate data

Since both datasets contain state-level information in the United States, the data can be combined based on the state name. Through this, the relationship between crime rates and socioeconomic indicators can be analyzed.


## Constraints

There might be several limitations which could affect the result. 

First, crime data may be influenced by differences in reporting practices across states, which may introduce inconsistency.

Second, the analysis is conducted at the state level, which may conceal any important variations within states.

Lastly, some indicators may not perfectly align in terms of time coverage with crime data and it may require filtering the datasets to overlapping years.

## Gaps

 Although there are two primary datasets in the current plan, there are some areas that need improvement.
One is that there are some socioeconomic factors, like education levels, population density, and urbanization, that could be helpful in further understanding the difference in crime rates. We could look into further datasets that could include these factors if necessary.

 Another is that, although we have included that we could merge these two datasets based on state-level information, we might have to further investigate if these two datasets have similar time and geographical units. This could be an issue if there are any discrepancies.

 Lastly, we might have to further investigate and get more information on how we could further choose appropriate statistical methods, like correlation and regression, in further evaluating how socioeconomic factors affect crime rates.

