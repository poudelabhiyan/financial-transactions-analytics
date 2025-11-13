import matplotlib.pyplot as plt


def plot_monthly_totals(monthly_df, save_path=None):
    """
    Line chart of monthly total credit and total debit.
    """
    # Convert month to string for nicer labels
    x = monthly_df["month"].astype(str)
    credit = monthly_df["Total Credit (Income)"]
    debit = monthly_df["Total Debit (Expense)"]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, credit, marker="o", label="Credit (Income)")
    ax.plot(x, debit, marker="o", label="Debit (Expense)")

    ax.set_title("Monthly Credit vs Debit")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    ax.legend()
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300)

    plt.show()


def plot_top_customers(top_customers_df, save_path=None):
    """
    Bar chart of top spending customers.
    """
    x = top_customers_df["Customer ID"].astype(str)
    y = top_customers_df["Total Spent"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x, y)

    ax.set_title("Top Spending Customers (Debit)")
    ax.set_xlabel("Customer ID")
    ax.set_ylabel("Total Spent")

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300)

    plt.show()


def plot_amount_distribution(df, save_path=None):
    """
    Boxplot of transaction amounts to show distribution and outliers.
    """
    amounts = df["amount"]

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.boxplot(amounts, vert=True, showfliers=True)

    ax.set_title("Distribution of Transaction Amounts")
    ax.set_ylabel("Amount")

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300)

    plt.show()
