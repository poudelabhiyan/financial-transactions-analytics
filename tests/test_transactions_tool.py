import pandas as pd

from src.transactions_tool import (
    clean_data,
    summarize_income_expenses,
    monthly_summary,
)

#updated sample data frame

def _sample_dataframe() -> pd.DataFrame:
    """
    Create a small in memory sample dataset for tests.
    """
    data = {
        "Date": ["2025-01-01", "2025-01-02", "2025-02-01"],
        "Amount": [1000.0, -200.0, -300.0],
        "Type": ["credit", "debit", "debit"],
        "Description": ["Salary", "Groceries", "Utilities"],
    }
    return pd.DataFrame(data)


def test_clean_data_basic():
    df_raw = _sample_dataframe()
    df_clean = clean_data(df_raw)

    # Date and amount should be converted and not null
    assert "date" in df_clean.columns
    assert "amount" in df_clean.columns
    assert df_clean["date"].notna().all()
    assert df_clean["amount"].notna().all()


def test_summarize_income_expenses_columns():
    df_raw = _sample_dataframe()
    df_clean = clean_data(df_raw)

    summary = summarize_income_expenses(df_clean)

    expected_columns = {"Total Income", "Total Expenses", "Net Balance"}
    assert expected_columns.issubset(set(summary.columns))


def test_monthly_summary_not_empty():
    df_raw = _sample_dataframe()
    df_clean = clean_data(df_raw)

    monthly = monthly_summary(df_clean)

    # There should be at least one monthly row
    assert not monthly.empty
    assert "year_month" in monthly.columns
