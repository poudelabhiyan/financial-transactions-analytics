<h2>Financial Transactions Summary Tool</h2>

This project is a collaborative mini-sprint completed using Agile practices. The goal is to develop a small but functional Python tool that loads, cleans, summarizes, and analyzes a financial transactions dataset. The focus is on teamwork, clear process, feature-based development, and producing modular functions that can be reused in future dashboards or analytics.

<h2>Sprint Goal</h2>

  - To build a clean and reusable Python tool that can read the financial dataset, prepare it, summarize income and expenses, identify top spending categories, detect unusual transactions, and generate monthly summaries, all through a collaborative and traceable Agile workflow.

<h2>Project Overview</h2>

This tool works with the financial_transactions.csv dataset and includes a set of modular Python functions that handle data loading, preparation, and analysis. Each function is developed under a specific user story and maintained through a branch-per-feature workflow on GitHub. The team uses Taiga for sprint tracking and user story management.

<h2>The project emphasizes:</h2>

  * Clean, readable, and well-structured Python code

  * Consistent GitHub practices with branches, commits, and pull requests

  * User stories with clear acceptance criteria

  * Collaborative development

  * Full traceability between code, user stories, and tasks

<h2>Repository Structure</h2>
Financial_Transactions_Summary_Tool/
│
├── src/
│   └── transactions_tool.py
│
├── data/
│   └── financial_transactions.csv
│
├── docs/
│   └── screenshots, reports, and notes
│
├── tests/
│   └── basic test scripts
│
├── README.md
└── .gitignore

<h2>User Story Branches, Owners, and Assigned Functions</h2>

The development process follows a strict branch-per-feature approach. Each user story has its own branch, and every branch is owned by specific team members. Work is merged into the main branch only after review and approval.

| **User Story**                    | **Branch Name**                      | **Assigned Members** | **Primary Function**                   |
| --------------------------------- | ------------------------------------ | -------------------- | -------------------------------------- |
| US1 – Read and Load Dataset       | `feature/US1-read-data`              | Yash                 | `read_data(filepath)`                  |
| US2 – Clean and Prepare Data      | `feature/US2-clean-data`             | Yash, Devarsh        | `clean_data(df)`                       |
| US3 – Income and Expense Summary  | `feature/US3-income-expense-summary` | Abhiyan, Devarsh     | `summarize_income_expenses(df)`        |
| US4 – Top Expense Categories      | `feature/US4-top-categories`         | Bibal                | `top_expense_categories(df, n=5)`      |
| US5 – Monthly Summary             | `feature/US5-monthly-summary`        | Abhiyan              | `monthly_summary(df)`                  |
| US6 – Detect Unusual Transactions | `feature/US6-unusual-transactions`   | Abhiyan              | `detect_unusual_transactions(df, ...)` |

