Assignment 2 – Financial Transactions Summary Tool

This repository contains the completed work for Assignment 2. The project applies Agile methodology to design and develop a modular Python tool capable of reading, cleaning, and summarizing a financial transactions dataset. Collaboration, task tracking, and sprint execution were carried out using Taiga and GitHub.

Sprint Goal

Develop a modular and reusable Python tool that processes financial_transactions.csv by loading the data, cleaning and preparing it, generating income and expense summaries, identifying top expense categories, producing monthly summaries, and detecting unusual transactions. All development activities must demonstrate traceability, collaboration, and adherence to Agile practices.

Team Members and Roles

Abhiyan Poudel – Product Owner

Yash – Developer (US1)

Bibal – Developer (US4)

Devarsh – Developer (US2)

Each member held responsibility for a set of user stories, corresponding tasks, and feature branches.

Repository Structure
Assignment2_FinancialTransactions/
│
├── data/
│   └── financial_transactions.csv
│
├── docs/
│   ├── Definition_of_Done.md
│   ├── Liftoff_Notes.md
│   ├── Sprint_Planning_and_User_Stories.md
│   └── Team_Charter.md
│
├── src/
│   ├── transactions_tool.py
│   └── visualization.py
│
├── tests/
│   └── test_transactions_tool.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md


The folder structure separates data, documentation, source code, and tests, ensuring clarity and maintainability.

User Stories and Assigned Branches

The sprint included six user stories. Each story was assigned to a specific team member and developed on a dedicated feature branch for traceability and version control discipline.

User Story	Branch Name	Owner	Primary Function in transactions_tool.py
US1 – Read and Load Dataset	feature/US1-read-data	Yash	read_data(filepath)
US2 – Clean and Prepare Data	feature/US2-clean-data	Devarsh	clean_data(df)
US3 – Income and Expense Summary	feature/US3-income-expense-summary	Abhiyan	summarize_income_expenses(df)
US4 – Top Expense Categories	feature/US4-top-categories	Bibal	top_expense_categories(df, n=5)
US5 – Monthly Summary	feature/US5-monthly-summary	Abhiyan	monthly_summary(df)
US6 – Detect Unusual Transactions	feature/US6-unusual-transactions	Abhiyan	detect_unusual_transactions(df, …)

Acceptance criteria, story points, and tasks for each story are documented within the Taiga project.

Collaboration and Workflow
GitHub Workflow

The main branch remains protected to ensure stability.

Developers work on their feature branches, committing incremental updates.

When a story is completed, a Pull Request (PR) is opened to merge the feature branch into main.

The Product Owner reviews PRs, provides feedback where necessary, and approves merges upon meeting the Definition of Done.

After merging, related Taiga tasks are moved to Done.

Taiga Workflow

The team maintained transparency and organization using Taiga’s workflow:

User stories with acceptance criteria and points

Corresponding tasks

Workflow columns: Backlog → New → In Progress → Testing → Done

All sprint progress was updated regularly to reflect real-time activity

Agile Process Overview
Team Liftoff

A liftoff session established the mission, vision, success priorities, communication rules, and Definition of Done. All records are included in the docs/ folder.

Sprint Planning

The team created a clear sprint goal, six well-defined user stories, acceptance criteria, and story point estimates. Each story was assigned to a member with a dedicated branch for implementation.

Development

Work proceeded in short, traceable increments. Team members used GitHub for version control, committed regularly, and opened pull requests for review. The process ensured continuous delivery of functional components.

Review and Reflection

A sprint reflection and a video presentation summarizing progress, challenges, and outcomes will be provided as part of the final deliverables.

Running the Tool

To execute or test the tool:

Ensure Python is installed.

Install required packages using:

pip install -r requirements.txt


Verify that financial_transactions.csv is located in the data/ directory.

Run main.py or import functions from src/transactions_tool.py to generate summaries.

The tool outputs income vs. expense summaries, top categories, monthly breakdowns, and unusual transaction indicators depending on the function invoked.
