# Sprint Planning – Assignment 2: Financial Transactions Summary Tool

**Date:** November 16, 2025  
**Sprint Duration:** 1 week  
**Team Members:**  
- Abhiyan Poudel  
- Bibal Adhikari  
- Devarsh Ketankumar Oza  
- Yash Milankumar Patel 

---

## 1. Sprint Goal

Develop a modular Python tool that can read, clean, and summarize the Financial Transactions dataset, providing clear income/expense summaries, top spending categories, unusual transaction detection, and monthly trends for basic financial insights.

---

## 2. User Stories, Acceptance Criteria, and Estimates

### US1 – View total income and expenses

**Story ID:** US1  
**As a** user  
**I want** to view total income and total expenses  
**So that** I can understand my overall financial balance.

**Acceptance Criteria:**

- A function calculates:
  - Total income
  - Total expenses
  - Net balance (income minus expenses)
- Output is clearly labeled (for example: “Total Income”, “Total Expenses”, “Net Balance”).
- Negative values (if any) are handled correctly and do not break the code.
- The function can be called from `main.py` and prints a readable summary.

**Story Points:** 3  
**Owner:** Abhiyan Poudel  

---

### US2 – Identify top expense categories

**Story ID:** US2  
**As a** user  
**I want** to see the top spending categories  
**So that** I can understand where most of my money is going.

**Acceptance Criteria:**

- A function groups expenses by category (for example, “Food”, “Rent”, “Transport”).
- Only expense transactions are included in the calculation (income is excluded).
- Output shows at least the top 5 categories by total spending.
- Results are sorted from highest to lowest spending.
- The function returns a DataFrame or structured result that can be reused later.

**Story Points:** 3  
**Owner:** Bibal Adhikari  

---

### US3 – Monthly income and expense summary

**Story ID:** US3  
**As a** user  
**I want** to see monthly summaries of income and expenses  
**So that** I can track trends over time.

**Acceptance Criteria:**

- A function groups transactions by year and month.
- For each month, the output shows:
  - Total income
  - Total expenses
  - Net balance
- Dates are parsed correctly as datetime values.
- Output is sorted in chronological order.
- The result can be printed in a readable format from `main.py`.

**Story Points:** 5  
**Owner:** Devarsh Ketankumar Oza  

---

### US4 – Detect unusually large transactions

**Story ID:** US4  
**As a** user  
**I want** to detect unusually large transactions  
**So that** I can spot potential errors or fraud.

**Acceptance Criteria:**

- A function identifies transactions above a certain threshold (for example, greater than a set amount or based on statistical rules such as mean + 3 * standard deviation).
- The threshold value is clearly visible in the code or passed as a parameter.
- Output lists the flagged transactions with:
  - Date
  - Description (if available)
  - Category
  - Amount
- The function handles both income and expense outliers.
- No errors occur when the dataset has no outliers.

**Story Points:** 5  
**Owner:** Yash Milankumar Patel  

---

### US5 – Clean and validate the dataset

**Story ID:** US5  
**As a** user  
**I want** the dataset to be cleaned and validated  
**So that** all summaries are based on reliable data.

**Acceptance Criteria:**

- A `clean_data` function:
  - Standardizes column names (lowercase, no spaces).
  - Converts dates to datetime format.
  - Ensures the amount column is numeric.
- Missing or invalid values in critical fields (date, amount) are handled:
  - Either removed or replaced using a clear rule.
- The function returns a cleaned DataFrame.
- The cleaned DataFrame is used by all other summary functions (US1–US4).

**Story Points:** 5  
**Owner:** Abhiyan Poudel  

---

### US6 – Export summary results

**Story ID:** US6  
**As a** user  
**I want** to export summary results  
**So that** I can use them in reports or dashboards later.

**Acceptance Criteria:**

- At least one summary result (for example, monthly summary or top expense categories) can be exported to a CSV file.
- The export function allows specifying an output file name or uses a clear default.
- The exported file is created in a logical folder (for example, `data/` or `output/`).
- The function prints a confirmation message with the output file path.

**Story Points:** 2  
**Owner:** Bibal Adhikari  

---

## 3. Task Breakdown by User Story

Below is a high-level task list to guide work in Taiga. Each bullet can be added as a task under the correct user story.

### US1 – View total income and expenses
- Load cleaned dataset.
- Implement `summarize_income_expenses` function.
- Format and print results in `main.py`.

### US2 – Identify top expense categories
- Identify column for transaction category.
- Implement `top_expense_categories` function.
- Validate results with sample checks.

### US3 – Monthly income and expense summary
- Extract year and month from date column.
- Implement `monthly_summary` function.
- Verify that each month appears once in the output.

### US4 – Detect unusually large transactions
- Decide on threshold rule (fixed amount or statistical).
- Implement `detect_outliers` or `detect_unusual_transactions` function.
- Test with a few sample transactions.

### US5 – Clean and validate the dataset
- Implement `read_data` function.
- Implement `clean_data` function (dates, amounts, column names).
- Ensure all other functions use the cleaned DataFrame.

### US6 – Export summary results
- Implement `export_summary_to_csv` function.
- Test export and open the CSV file to confirm structure.

---

## 4. Taiga and GitHub Links (to be updated by team)

- **Taiga Project URL:** _https://tree.taiga.io/project/poudelabhiyan-assignment-2-financial-transactions-summary-tool/timeline_  
- **GitHub Repository URL:** _[https://github.com/poudelabhiyan/Assignment2_FinancialTransactions]_  

_End of Sprint Planning document._
