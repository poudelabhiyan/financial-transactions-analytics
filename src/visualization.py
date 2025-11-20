import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

# Make sure we can import from src when running directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.transactions_tool import (
    read_data,
    clean_data,
    summarize_income_expenses,
    top_expense_categories,
    monthly_summary,
    detect_unusual_transactions,
)

# -----------------------------------------------------------
# US1 – Read and Load Dataset: Overview of transaction types
# -----------------------------------------------------------
def plot_us1_dataset_overview(df_raw: pd.DataFrame) -> None:
    """
    Visual 1 (US1): Bar chart of transaction counts by type (credit / debit).
    """
    df = df_raw.copy()
    if "Type" in df.columns:
        df["Type"] = df["Type"].astype(str).str.strip().str.lower()
        counts = df["Type"].value_counts()
    elif "type" in df.columns:
        counts = df["type"].value_counts()
    else:
        print("No 'type' or 'Type' column found for US1 overview.")
        return

    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar")
    plt.title("US1 – Transactions by Type (Raw Data)")
    plt.xlabel("Transaction Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# US2 – Clean and Prepare Data: Rows before vs after cleaning
# -----------------------------------------------------------
def plot_us2_cleaning_effect(df_raw: pd.DataFrame, df_clean: pd.DataFrame) -> None:
    """
    Visual 2 (US2): Bar chart showing number of rows before and after cleaning.
    """
    counts = pd.Series(
        {
            "Before Cleaning": len(df_raw),
            "After Cleaning": len(df_clean),
        }
    )

    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar")
    plt.title("US2 – Rows Before vs After Cleaning")
    plt.ylabel("Number of Rows")
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# US3 – Income and Expense Summary: Total Income vs Expenses
# -----------------------------------------------------------
def plot_us3_income_expense(df_clean: pd.DataFrame) -> None:
    """
    Visual 3 (US3): Bar chart of Total Income vs Total Expenses vs Net Balance.
    """
    summary = summarize_income_expenses(df_clean)

    # summary is a 1-row DataFrame
    values = summary.iloc[0][["Total Income", "Total Expenses", "Net Balance"]]

    plt.figure(figsize=(6, 4))
    values.plot(kind="bar")
    plt.title("US3 – Income, Expenses, and Net Balance")
    plt.ylabel("Amount")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# US4 – Top Expense Categories
# -----------------------------------------------------------
def plot_us4_top_categories(df_clean: pd.DataFrame, top_n: int = 5) -> None:
    """
    Visual 4 (US4): Top N expense categories by total expense.
    """
    top_cats = top_expense_categories(df_clean, top_n=top_n)

    if top_cats.empty:
        print("US4 – No expense category data available.")
        return

    plt.figure(figsize=(8, 4))
    plt.bar(top_cats["category"], top_cats["total_expense"])
    plt.title(f"US4 – Top {top_n} Expense Categories")
    plt.xlabel("Category")
    plt.ylabel("Total Expense")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# US5 – Monthly Summary: Monthly Net Balance
# -----------------------------------------------------------
def plot_us5_monthly_net_balance(df_clean: pd.DataFrame) -> None:
    """
    Visual 5 (US5): Line chart of monthly net balance over time.
    """
    monthly = monthly_summary(df_clean)
    if monthly.empty:
        print("US5 – Monthly summary is empty.")
        return

    monthly_sorted = monthly.sort_values("year_month")
    x = monthly_sorted["year_month"].astype(str)
    y = monthly_sorted["Net Balance"]

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, marker="o")
    plt.title("US5 – Monthly Net Balance")
    plt.xlabel("Year-Month")
    plt.ylabel("Net Balance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# US6 – Detect Unusual Transactions: Scatter of amounts
# -----------------------------------------------------------
def plot_us6_unusual_transactions(df_clean: pd.DataFrame, threshold=None) -> None:
    """
    Visual 6 (US6): Scatter plot of transaction amounts,
    highlighting unusual transactions.
    """
    df = df_clean.copy()

    # Detect unusual transactions using your function
    unusual = detect_unusual_transactions(df, threshold=threshold)

    if "date" not in df.columns:
        print("US6 – 'date' column is missing; using index instead.")
        x_all = range(len(df))
        x_unusual = unusual.index
        x_label = "Index"
    else:
        x_all = df["date"]
        x_unusual = unusual["date"]
        x_label = "Date"

    plt.figure(figsize=(10, 4))
    plt.scatter(x_all, df["amount"], alpha=0.4, label="All Transactions")

    if not unusual.empty:
        plt.scatter(x_unusual, unusual["amount"], color="red", label="Unusual", zorder=3)

    plt.title("US6 – Unusual Transactions Detection")
    plt.xlabel(x_label)
    plt.ylabel("Amount")
    plt.legend()
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# Run all 6 visuals in sequence
# -----------------------------------------------------------
def run_all_user_story_visuals():
    # 1. Load raw data
    df_raw = read_data("data/financial_transactions.csv")

    # 2. Clean data
    df_clean = clean_data(df_raw)

    print("Raw shape:", df_raw.shape)
    print("Cleaned shape:", df_clean.shape)

    # US1 visual
    print("\n[US1] Dataset overview – transactions by type")
    plot_us1_dataset_overview(df_raw)

    # US2 visual
    print("\n[US2] Cleaning effect – rows before vs after")
    plot_us2_cleaning_effect(df_raw, df_clean)

    # US3 visual
    print("\n[US3] Income vs expenses summary")
    plot_us3_income_expense(df_clean)

    # US4 visual
    print("\n[US4] Top expense categories")
    plot_us4_top_categories(df_clean, top_n=5)

    # US5 visual
    print("\n[US5] Monthly net balance over time")
    plot_us5_monthly_net_balance(df_clean)

    # US6 visual
    print("\n[US6] Unusual transactions scatter")
    plot_us6_unusual_transactions(df_clean, threshold=None)


if __name__ == "__main__":
    run_all_user_story_visuals()
