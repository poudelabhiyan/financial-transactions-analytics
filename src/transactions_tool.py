from pathlib import Path
import pandas as pd
# Minor clarity update by Abhiyan for US5


def read_data(filepath: str) -> pd.DataFrame:
    # Small update added by Yash for Agile assignment for US2
    """
    Read the financial transactions CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Raw transactions data.
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # small change in clean data US2
    """
    Clean and standardize the transactions dataset.

    - Standardizes column names.
    - Converts 'date' to datetime.
    - Converts 'amount' to numeric.
    - Drops rows with missing date or amount.
    - Normalizes the 'type' column (credit / debit).

    Parameters
    ----------
    df : pd.DataFrame
        Raw transactions data.

    Returns
    -------
    pd.DataFrame
        Cleaned transactions data.
    """
    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert data types
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Normalize transaction type
    if "type" in df.columns:
        df["type"] = df["type"].astype(str).str.strip().str.lower()

    # Drop rows with missing critical fields
    df = df.dropna(subset=["date", "amount"])

    return df


def summarize_income_expenses(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total income, total expenses, and net balance.

    Income is assumed to be rows where type == 'credit'.
    Expenses are rows where type == 'debit'.

    Returns a one-row DataFrame with:
    - Total Income
    - Total Expenses
    - Net Balance
    """
    df = df.copy()

    total_income = df.loc[df["type"] == "credit", "amount"].sum()
    total_expenses = df.loc[df["type"] == "debit", "amount"].sum()

    net_balance = total_income - total_expenses

    summary = pd.DataFrame(
        {
            "Total Income": [total_income],
            "Total Expenses": [total_expenses],
            "Net Balance": [net_balance],
        }
    )

    return summary

# US4:- Top Speding Customers (by devarsh)
def top_expense_categories(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """
    Identify the top expense categories by total amount.

    NOTE:
    The provided dataset does not include a natural 'category' column.
    For now, this function assumes that a 'category' column
    may be added later. If it is missing, all expenses are
    treated as a single 'General' category.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned transactions.
    top_n : int
        Number of top categories to return.

    Returns
    -------
    pd.DataFrame
        Categories and their total expense amounts, sorted
        from highest to lowest.
    """
    df = df.copy()

    # Work only with expenses
    expenses = df.loc[df["type"] == "debit"].copy()

    if expenses.empty:
        return pd.DataFrame(columns=["category", "total_expense"])

    # If no category column exists yet, use a placeholder
    if "category" not in expenses.columns:
        expenses["category"] = "General"

    grouped = (
        expenses.groupby("category", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_expense"})
        .sort_values("total_expense", ascending=False)
        .head(top_n)
    )

    return grouped


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a monthly summary of income, expenses, and net balance.

    Groups data by year and month.

    Returns a DataFrame with:
    - year_month (YYYY-MM)
    - Total Income
    - Total Expenses
    - Net Balance
    """
    df = df.copy()

    if "date" not in df.columns:
        raise ValueError("Column 'date' is required for monthly summary.")

    df["year_month"] = df["date"].dt.to_period("M")

    pivot = (
        df.groupby(["year_month", "type"])["amount"]
        .sum()
        .unstack(fill_value=0)
    )

    # Handle missing credit/debit columns safely
    total_income = pivot.get("credit", pd.Series(0, index=pivot.index))
    total_expenses = pivot.get("debit", pd.Series(0, index=pivot.index))

    result = pd.DataFrame(
        {
            "year_month": pivot.index.astype(str),
            "Total Income": total_income.values,
            "Total Expenses": total_expenses.values,
        }
    )

    result["Net Balance"] = result["Total Income"] - result["Total Expenses"]

    return result


def detect_unusual_transactions(
    df: pd.DataFrame,
    threshold: Optional[float] = None
) -> pd.DataFrame:
    """
    Detect unusually large transactions.

    If a threshold is provided, any transaction with an absolute
    amount greater than or equal to that threshold is flagged.

    If no threshold is provided, a statistical rule is used:
    amount >= mean + 3 * standard deviation.

    Returns a DataFrame of flagged transactions.
    """
    df = df.copy()

    if df["amount"].empty:
        return df.iloc[0:0]

    if threshold is not None:
        mask = df["amount"].abs() >= threshold
    else:
        mean = df["amount"].mean()
        std = df["amount"].std()
        limit = mean + 3 * std
        mask = df["amount"].abs() >= limit

    outliers = df.loc[mask].copy()
    return outliers


def export_summary_to_csv(summary_df: pd.DataFrame, output_path: str) -> None:
    """
    Export a summary DataFrame (for example monthly or category summary)
    to a CSV file.

    Parameters
    ----------
    summary_df : pd.DataFrame
        Summary data to export.
    output_path : str
        Target CSV path, for example 'output/monthly_summary.csv'.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_df.to_csv(output_path, index=False)
    print(f"Summary exported to: {output_path.resolve()}")
