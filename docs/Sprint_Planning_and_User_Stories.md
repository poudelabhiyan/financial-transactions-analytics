<h1>Sprint Planning and User Stories</h1>

<h2>Assignment 2: Financial Transactions Summary Tool</h2>
Date: November 13, 2025
Sprint Duration: 1 Week
Team Members: Abhiyan Poudel, Bibal Adhikari, Devarsh Ketankumar Oza, Yash Milankumar Patel

<h2>Sprint Goal</h2>

To deliver a functional Python tool capable of loading, cleaning, and summarizing a financial transactions dataset. The tool should provide clear insights such as total income, total expenses, top spending categories, monthly summaries, and unusual transactions. All development must follow Agile practices and demonstrate effective collaboration through GitHub and Taiga.

<h2>Sprint Overview</h2>

The team planned the sprint using Taiga, created user stories with acceptance criteria, estimated story effort, and assigned each story to designated team members.
A branch-per-feature workflow was established on GitHub to ensure traceability and clean version control.
The sprint focuses on delivering a minimal but working version of the tool with clean code, readable output, and consistent collaboration across all members.

<h2>User Stories</h2>
<h3>US1 — Read and Load the Dataset</h3>

Story:
As a user, I want the program to load the financial transactions file so that I can work with the data inside Python.

<h3>Acceptance Criteria:</h3>

* The CSV file loads without errors.

* All expected columns appear correctly.

* Invalid file paths return a clear error message.

* The output is a clean DataFrame ready for processing.

Assigned To: Yash
Branch: feature/US1-read-data

<h3>US2 — Clean and Prepare the Data</h3>

Story:
As a user, I want the dataset to be cleaned and prepared so that I can analyze it without issues.

<h3>Acceptance Criteria:</h3>

* Column names follow a consistent format.

* Missing or invalid values are handled appropriately.

* Amounts and dates are converted to proper data types.

* Cleaned output is ready for further analysis.

Assigned To: Yash, Devarsh
Branch: feature/US2-clean-data

<h3>US3 — Income and Expense Summary</h3>

Story:
As a user, I want a summary of total income, total expenses, and net balance so that I can quickly understand my financial overview.

<h3>Acceptance Criteria:</h3>

* Income (positive amounts) is summed accurately.

* Expenses (negative amounts) are summed accurately.

* Net total is calculated correctly.

* Output is clear, readable, and easy to interpret.

Assigned To: Abhiyan, Devarsh
Branch: feature/US3-income-expense-summary

<h3>US4 — Top Expense Categories</h3>

Story:
As a user, I want to see my top spending categories so that I can understand where most of my money goes.

<h3>Acceptance Criteria:</h3>

* Categories are grouped and sorted by total expense amount.

* The top 5 categories are displayed.

* Missing category values are handled safely.

* Results are formatted clearly.

Assigned To: Bibal
Branch: feature/US4-top-categories

<h3>US5 — Monthly Summary</h3>

Story:
As a user, I want a month-by-month breakdown of income and expenses so that I can understand financial trends over time.

<h3>Acceptance Criteria:</h3>

* Transactions are grouped correctly by month.

* Monthly income, expenses, and net totals are displayed.

* Date parsing is handled without errors.

* Output is easy to read and interpret.

Assigned To: Abhiyan
Branch: feature/US5-monthly-summary

<h3>US6 — Detect Unusual Transactions</h3>

Story:
As a user, I want unusual or suspicious transactions to be highlighted so that I can review them manually.

<h3>Acceptance Criteria:</h3>

* A logical rule identifies unusual values (e.g., extremely high amounts).

* Output clearly lists unusual transactions.

* The method handles unexpected values safely.

* The user can easily understand why a transaction is flagged.

Assigned To: Abhiyan
Branch: feature/US6-unusual-transactions

<h2>Task Breakdown</h2>

* Each user story includes the following tasks:

* Review the dataset to understand required fields

* Create or update the function linked to the story

* Test the function with sample data

* Commit changes with a clear message referencing the US number

* Push updates to the corresponding feature branch

* Open a Pull Request for code review

* Move the task through Taiga: New → In Progress → Testing → Done

<h2>Sprint Planning Outcomes</h2>

By the end of the sprint planning session, the team finalized:

* A clear and achievable sprint goal

* Six user stories with well-defined acceptance criteria

* Story assignments for all team members

* Feature branches created for each user story

* Tasks added and organized in Taiga

* Agreement on the collaboration workflow, communication process, and code review standards

With planning complete, the team has moved into the development phase of the sprint.
