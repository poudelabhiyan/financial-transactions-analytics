from src.transactions_tool import (
    read_data,
    clean_data,
    summarize_income_expenses,
    top_expense_categories,
    monthly_summary,
    detect_unusual_transactions,
    export_summary_to_csv,
)


def main() -> None:
    """
    Simple demo runner for the Financial Transactions Summary Tool.

    This script:
    1. Reads the CSV file.
    2. Cleans the data.
    3. Prints income and expense summary.
    4. Prints top expense categories.
    5. Prints monthly summary.
    6. Detects unusual transactions.
    7. Exports one summary to CSV.
    """
    data_path = "financial_transactions.csv"

    print("Reading data...")
    df_raw = read_data(data_path)

    print("Cleaning data...")
    df_clean = clean_data(df_raw)

    print("\nIncome and expense summary")
    income_expense_summary = summarize_income_expenses(df_clean)
    print(income_expense_summary.to_string(index=False))

    print("\nTop expense categories")
    top_categories = top_expense_categories(df_clean, top_n=5)
    if not top_categories.empty:
        print(top_categories.to_string(index=False))
    else:
        print("No expense data available or categories not defined yet.")

    print("\nMonthly income and expense summary")
    monthly = monthly_summary(df_clean)
    print(monthly.to_string(index=False))

    print("\nUnusually large transactions (automatic threshold)")
    unusual_auto = detect_unusual_transactions(df_clean, threshold=None)
    if unusual_auto.empty:
        print("No unusual transactions found based on the current rule.")
    else:
        print(unusual_auto.to_string(index=False))

    print("\nExporting monthly summary to CSV...")
    export_summary_to_csv(monthly, "output/monthly_summary.csv")
    print("Done.")


if __name__ == "__main__":
    main()
