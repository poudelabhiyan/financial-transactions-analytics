from src.transactions_tool import (
    read_data,
    clean_data,
    summarize_income_expenses,
    top_expense_customers,
    detect_outliers,
    monthly_summary,
)


def main():
    # 1. Load data from the data folder
    filepath = "data/financial_transactions.csv"
    df_raw = read_data(filepath)
    print("Raw data shape:", df_raw.shape)

    # 2. Clean data
    df_clean = clean_data(df_raw)
    print("Clean data shape:", df_clean.shape)

    # 3. Income vs expense summary
    print("\nIncome and Expense Summary")
    summary = summarize_income_expenses(df_clean)
    print(summary)

    # 4. Top spending customers
    print("\nTop Expense Customers")
    top_customers = top_expense_customers(df_clean, n=5)
    print(top_customers)

    # 5. Monthly summary
    print("\nMonthly Summary (first 10 rows)")
    monthly = monthly_summary(df_clean)
    print(monthly.head(10))

    # 6. Outliers
    print("\nOutlier Transactions (first 10 rows)")
    outliers = detect_outliers(df_clean)
    print(outliers.head(10))


if __name__ == "__main__":
    main()
