"""
scripts/clean_and_merge.py

Data Integration Script — IS 477 Final Project: fuelthedata

Loads, cleans, and merges three datasets:
  - PovertyReport.xlsx        (USDA ERS poverty estimates 2023)
  - UnemploymentReport.xlsx   (USDA ERS unemployment & median income)
  - CIUS_Table_8_...xlsx      (FBI UCR offenses known to law enforcement 2024)

Output:
  - results/merged_data.csv   (merged state-level dataset)

Usage:
  python scripts/clean_and_merge.py
"""

import pandas as pd
import os

POVERTY_PATH  = "data/PovertyReport.xlsx"
UNEMPLOY_PATH = "data/UnemploymentReport.xlsx"
CRIME_PATH    = ("data/offenses-known-to-le-2024/"
                 "CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx")
OUTPUT_PATH   = "results/merged_data.csv"

# ── Load ───────────────────────────────────────────────────────────────────────
print("Loading datasets...")
poverty      = pd.read_excel(POVERTY_PATH,  skiprows=5)
unemployment = pd.read_excel(UNEMPLOY_PATH, skiprows=3)
crime        = pd.read_excel(CRIME_PATH,    skiprows=3)

poverty = poverty[['Name', 'Percent']].rename(columns={
    'Name':    'State',
    'Percent': 'Poverty Rate'
})
poverty = poverty[poverty['State'] != 'National']  # drop national aggregate row
poverty = poverty.dropna(subset=['State', 'Poverty Rate'])
print(f"Poverty dataset: {poverty.shape}")

unemployment = unemployment[['Name', '2023', 'Median Household Income (2022)']].rename(columns={
    'Name': 'State',
    '2023': 'Unemployment Rate'
})
unemployment = unemployment.dropna(subset=['State', 'Unemployment Rate'])

# Remove $ and , from income column and convert to numeric
unemployment['Median Household Income (2022)'] = (
    unemployment['Median Household Income (2022)']
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .pipe(pd.to_numeric, errors='coerce')
)
print(f"Unemployment dataset: {unemployment.shape}")

crime.columns = crime.columns.str.replace('\n', ' ').str.strip()

crime_cols = [
    'State',
    'Violent crime',
    'Murder and nonnegligent manslaughter',
    'Rape',
    'Robbery',
    'Aggravated assault',
    'Property crime',
    'Burglary',
    'Larceny- theft',
    'Motor vehicle theft'
]
crime = crime[crime_cols]

# Aggregate city-level to state level
crime_state = crime.groupby('State').sum().reset_index()
crime_state['State'] = crime_state['State'].str.title()
print(f"Crime dataset (after aggregation): {crime_state.shape}")

print("\nMerging datasets...")
merged = poverty.merge(unemployment, on='State')
merged = merged.merge(crime_state, on='State')

print(f"Merged dataset shape: {merged.shape}")
print(merged.head())

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
merged.to_csv(OUTPUT_PATH, index=False)
print(f"\nSaved merged dataset to: {OUTPUT_PATH}")
