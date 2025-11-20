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
<img width="393" height="458" alt="image" src="https://github.com/user-attachments/assets/23e5f9f1-d887-4f2a-9514-a18f82d894f7" />



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

<h2>How to Run the Tool</h2>

  * Clone the repository

  * Ensure the dataset is placed in the data/ folder

  * Install required Python packages such as pandas and numpy

  * Import the module and call the functions as needed

Example:

from src.transactions_tool import *

  df = read_data("data/financial_transactions.csv")

  df_clean = clean_data(df)

  summary = summarize_income_expenses(df_clean)

<h2>Collaboration and Workflow</h2>

The team follows the Agile process closely:

<h3>GitHub Workflow</h3>

  * Each story is developed in its own feature branch

  * Every commit references the user story ID (e.g., "US3: added income summary logic")

  * Pull requests are reviewed before merging

  * Code is kept clean, modular, and well documented

<h3>Taiga Workflow</h3>

  * All user stories and tasks are tracked in a private Taiga project

  * Tasks move from Backlog → To Do → In Progress → Testing → Done

  * Story points and acceptance criteria are recorded

  * Daily updates and continuous progress are maintained throughout the sprint

<h2>Core Functions in the Tool</h2>

The main Python functions include:

read_data(filepath)

clean_data(df)

summarize_income_expenses(df)

top_expense_categories(df, n=5)

monthly_summary(df)

detect_unusual_transactions(df, ...)

Each function is tied directly to a user story and developed under its respective feature branch.

<h2>Testing and Validation</h2>

Basic tests or assertion checks are added to ensure each function produces accurate and consistent results. These tests help validate logic and improve the reliability of the tool.

<h2>Sprint Deliverables</h2>

- Team Liftoff Summary

- Sprint Goal

- User Stories and Acceptance Criteria

- Python Module (transactions_tool.py)

- GitHub Commit History

- Taiga Board Screenshot


