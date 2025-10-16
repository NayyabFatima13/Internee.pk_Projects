
# DATA CLEANING AND PREPROCESSING SCRIPT
# For internship_applications_dirty.csv

import pandas as pd
import numpy as np
from datetime import datetime

def clean_internship_data(df):
    """Comprehensive data cleaning function"""
    
    # Create a copy to preserve original data
    cleaned_df = df.copy()
    
    # 1. STANDARDIZE TEXT FIELDS
    text_columns = ['first_name', 'last_name', 'university', 'major', 'position_applied']
    for col in text_columns:
        cleaned_df[col] = cleaned_df[col].astype(str).str.strip().str.title()
    
    # 2. CLEAN EMAIL ADDRESSES
    cleaned_df['email'] = cleaned_df['email'].str.lower().str.replace(' at ', '@').str.strip()
    
    # 3. STANDARDIZE PHONE NUMBERS
    # Remove non-numeric characters and format consistently
    cleaned_df['phone_number'] = cleaned_df['phone_number'].astype(str).str.replace(r'\D', '', regex=True)
    
    # 4. HANDLE MISSING VALUES
    # GPA: Fill with mean or median
    gpa_mean = pd.to_numeric(cleaned_df['gpa'], errors='coerce').mean()
    cleaned_df['gpa'] = pd.to_numeric(cleaned_df['gpa'], errors='coerce').fillna(gpa_mean)
    
    # Years of experience: Fill with 0 for interns
    cleaned_df['years_of_experience'] = cleaned_df['years_of_experience'].fillna(0)
    
    # 5. FIX DATA TYPES
    cleaned_df['application_date'] = pd.to_datetime(cleaned_df['application_date'], errors='coerce')
    cleaned_df['graduation_year'] = pd.to_numeric(cleaned_df['graduation_year'], errors='coerce')
    
    # 6. HANDLE OUTLIERS
    # Cap unrealistic values
    cleaned_df['gpa'] = cleaned_df['gpa'].clip(0, 4.0)
    cleaned_df['years_of_experience'] = cleaned_df['years_of_experience'].clip(0, 10)
    
    # 7. STANDARDIZE CATEGORICAL VARIABLES
    status_mapping = {'review': 'Under Review', 'accepted': 'Accepted', 'rejected': 'Rejected'}
    cleaned_df['application_status'] = cleaned_df['application_status'].str.strip().str.title()
    cleaned_df['application_status'] = cleaned_df['application_status'].replace(status_mapping)
    
    # 8. REMOVE DUPLICATES
    cleaned_df = cleaned_df.drop_duplicates()
    cleaned_df = cleaned_df.drop_duplicates(subset=['email', 'first_name', 'last_name'])
    
    # 9. CREATE DERIVED COLUMNS
    cleaned_df['full_name'] = cleaned_df['first_name'] + ' ' + cleaned_df['last_name']
    cleaned_df['days_since_application'] = (datetime.now() - cleaned_df['application_date']).dt.days
    
    return cleaned_df

# Load and clean the data
df = pd.read_csv('dirty_internship_applications.csv')
cleaned_df = clean_internship_data(df)

print("Data cleaning completed!")
print(f"Original shape: {df.shape}")
print(f"Cleaned shape: {cleaned_df.shape}")
