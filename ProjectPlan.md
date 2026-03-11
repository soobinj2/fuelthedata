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

## Gaps

