import pandas as pd
import numpy as np


def read_data(filepath: str) -> pd.DataFrame:
    """
    Load the dataset and return a DataFrame.
    """
    df = pd.read_csv(filepath)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
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


def summarize_income_expenses(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize total credits and debits and compute net balance.
    'credit' = income (money in)
    'debit'  = expense (money out)
    """
    df = df.copy()

    # clean the type column for consistency
    df['type'] = df['type'].astype(str).str.strip().str.lower()

    total_credit = df[df['type'] == 'credit']['amount'].sum()
    total_debit = df[df['type'] == 'debit']['amount'].sum()
    net_balance = total_credit - total_debit

    summary = pd.DataFrame({
        'Total Credit (Income)': [total_credit],
        'Total Debit (Expense)': [total_debit],
        'Net Balance': [net_balance]
    })

    return summary


def top_expense_customers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Return the top n customers with the highest total debit (expense) amounts.
    Uses 'customer_id' since no category column exists.
    """
    df = df.copy()
    df['type'] = df['type'].astype(str).str.strip().str.lower()

    expense_df = df[df['type'] == 'debit']

    top_expenses = (
        expense_df.groupby('customer_id')['amount']
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

    top_expenses.columns = ['Customer ID', 'Total Spent']
    return top_expenses


def detect_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect transactions with unusually high or low amounts using the IQR method.
    Returns a DataFrame of outlier transactions.
    """
    df = df.copy()
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    q1 = df['amount'].quantile(0.25)
    q3 = df['amount'].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[(df['amount'] < lower_bound) | (df['amount'] > upper_bound)]

    return outliers


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a monthly summary of total credits and debits.
    Groups transactions by month and type ('credit' or 'debit').
    """
    df = df.copy()

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.to_period('M')

    df['type'] = df['type'].astype(str).str.strip().str.lower()

    monthly = (
        df.groupby(['month', 'type'])['amount']
        .sum()
        .unstack(fill_value=0)
        .reset_index()
        .sort_values('month')
    )

    monthly.columns.name = None
    monthly = monthly.rename(columns={
        'credit': 'Total Credit (Income)',
        'debit': 'Total Debit (Expense)'
    })

    return monthly
