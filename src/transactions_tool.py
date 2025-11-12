import pandas as pd
import numpy as np
# 1. Load the dataset
def read_data(filepath):
    df = pd.read_csv(filepath)
    print("Data loaded successfully. Shape:", df.shape)
    return df
df = read_data("financial_transactions.csv")
df.head(5)
df.isnull().sum()

# 2. Clean and prepare the dataset
def clean_data(df):
    """
    Clean column names, fix data types, and handle missing values.
    """
    df = df.copy()
    # standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )

    # ensure proper data types
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    return df

clean_df = clean_data(df)
clean_df.head()

def summarize_income_expenses(df):
    """Summarize total credits and debits and compute net balance. 
    'credit' = income (money in)
    'debit'  = expense (money out)
    """
    # Clean the type column for consistency
    df['type'] = df['type'].astype(str).str.strip().str.lower()

    # Calculate totals
    total_credit = df[df['type'] == 'credit']['amount'].sum()
    total_debit = df[df['type'] == 'debit']['amount'].sum()
    net_balance = total_credit - total_debit

    # Create summary table
    summary = pd.DataFrame({
        'Total Credit (Income)': [total_credit],
        'Total Debit (Expense)': [total_debit],
        'Net Balance': [net_balance]
    })
    
    return summary
summary_table = summarize_income_expenses(clean_df)
summary_table

def top_expense_categories(df, n=5):
    """
    Return the top n customers with the highest total debit (expense) amounts. Uses 'customer_id' since no category column exists.
    """
    df['type'] = df['type'].astype(str).str.strip().str.lower()

    # Filter only debit (expense) transactions
    expense_df = df[df['type'] == 'debit']

    # Group by customer_id and sum amounts
    top_expenses = (
        expense_df.groupby('customer_id')['amount']
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

    top_expenses.columns = ['Customer ID', 'Total Spent']
    return top_expenses

top_expenses = top_expense_categories(clean_df)
top_expenses

def detect_outliers(df):
    """
    Detect transactions with unusually high or low amounts using the IQR (Interquartile Range) method.
    Returns a DataFrame of outlier transactions.
    """
    # Ensure the 'amount' column is numeric
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    
    # Compute Q1 (25th percentile) and Q3 (75th percentile)
    q1 = df['amount'].quantile(0.25)
    q3 = df['amount'].quantile(0.75)
    iqr = q3 - q1

    # Define lower and upper bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Filter transactions outside the bounds
    outliers = df[(df['amount'] < lower_bound) | (df['amount'] > upper_bound)]

    print(f"Detected {len(outliers)} outlier transactions.")
    return outliers

outliers = detect_outliers(clean_df)
outliers.head()
def monthly_summary(df):
    """
    Create a monthly summary of total credits and debits.
    Groups transactions by month and type ('credit' or 'debit').
    Returns a DataFrame showing monthly totals.
    """
    # Ensure the date column is in datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Extract the month (YYYY-MM format)
    df['month'] = df['date'].dt.to_period('M')

    # Normalize 'type' values
    df['type'] = df['type'].astype(str).str.strip().str.lower()

    # Group by month and type, sum the amount
    monthly = (
        df.groupby(['month', 'type'])['amount']
        .sum()
        .unstack(fill_value=0)
        .reset_index()
        .sort_values('month')
    )

    # Rename columns for clarity
    monthly.columns.name = None
    monthly = monthly.rename(columns={
        'credit': 'Total Credit (Income)',
        'debit': 'Total Debit (Expense)'
    })

    return monthly
monthly_summary_df = monthly_summary(clean_df)
monthly_summary_df.head(10)
