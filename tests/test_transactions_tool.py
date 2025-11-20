import os
import sys
import pandas as pd

# -----------------------------------------------------
# FIX IMPORT PATH FOR LOCAL TESTING
# Ensures Python can import from src/ when running tests in CMD
# -----------------------------------------------------
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.transactions_tool import (
    read_data,
    clean_data,
    summarize_income_expenses,
    top_expense_categories,
    monthly_summary,
    detect_unusual_transactions,
)

# -----------------------------------------------------
# SAMPLE DATAFRAME FOR TESTING
# -----------------------------------------------------
def _sample_dataframe() -> pd.DataFrame:
    data = {
        "Date": ["2025-01-01", "2025-01-02", "2025-02-01"],
        "Amount": [1000.0, -200.0, -300.0],
        "Type": ["credit", "debit", "debit"],
        "Description": ["Salary", "Groceries", "Utilities"],
    }
    return pd.DataFrame(data)


# -----------------------------------------------------
# TEST read_data()
# -----------------------------------------------------
def test_read_data_file_not_found():
    try:
        read_data("nonexistent.csv")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True


# -----------------------------------------------------
# TEST clean_data()
# -----------------------------------------------------
def test_clean_data_basic():
    df_raw = _sample_dataframe()
    df_clean = clean_data(df_raw)

    assert "date" in df_clean.columns
    assert "amount" in df_clean.columns
    assert df_clean["date"].notna().all()
    assert df_clean["amount"].notna().all()


# -----------------------------------------------------
# TEST summarize_income_expenses()
# -----------------------------------------------------
def test_summarize_income_expenses_columns():
    df = clean_data(_sample_dataframe())
    summary = summarize_income_expenses(df)

    expected_columns = {"Total Income", "Total Expenses", "Net Balance"}
    assert expected_columns.issubset(set(summary.columns))


# -----------------------------------------------------
# TEST top_expense_categories()
# -----------------------------------------------------
def test_top_expense_categories_default():
    df = clean_data(_sample_dataframe())
    result = top_expense_categories(df)

    assert "category" in result.columns
    assert "total_expense" in result.columns


# -----------------------------------------------------
# TEST monthly_summary()
# -----------------------------------------------------
def test_monthly_summary_not_empty():
    df = clean_data(_sample_dataframe())
    monthly = monthly_summary(df)

    assert not monthly.empty
    assert "year_month" in monthly.columns


# -----------------------------------------------------
# TEST detect_unusual_transactions()
# -----------------------------------------------------
def test_detect_unusual_transactions_threshold():
    df = clean_data(_sample_dataframe())
    result = detect_unusual_transactions(df, threshold=500)

    # Should detect the income 1000.0
    assert not result.empty
    assert result.iloc[0]["amount"] == 1000.0
