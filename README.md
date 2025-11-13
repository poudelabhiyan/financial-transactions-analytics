Assignment 2 – Financial Transactions Summary Tool
Course: CPSC-620 (Version Control and Agile Collaboration)
Team Members

Abhiyan Poudel

Bibal Adhikari

Devarsh Ketankumar Oza

Yash Milankumar Patel

Project Overview

The Financial Transactions Summary Tool is a modular Python application that analyzes a dataset of financial transactions.
It loads a CSV file, cleans and processes the data, and generates meaningful insights such as total income, total expenses, top spending customers, monthly financial trends, and outlier detection.
The project follows Agile values, iterative development, and collaborative version control practices using GitHub and Taiga.

Key Objectives

Apply Agile teamwork principles such as branching, incremental development, and pull requests.

Build a set of reusable Python functions for data loading, cleaning, summarizing, and visualization.

Demonstrate clean coding practices, modular design, and maintainable structure.

Produce clear documentation including a Team Charter, Liftoff Notes, and Definition of Done.

Repository Structure
Assignment2_FinancialTransactions/
│
├── data/
│   └── financial_transactions.csv
│
├── docs/
│   ├── Team_Charter.md
│   ├── Liftoff_Notes.md
│   └── Definition_of_Done.md
│
├── src/
│   ├── transactions_tool.py        # Main analysis functions
│   └── visualization.py            # Matplotlib visualizations
│
├── tests/
│   └── .keep                       # Placeholder for future test files
│
├── main.py                         # Runs all summaries and visual outputs
├── README.md
└── .gitignore

Core Features
✔ Data Processing

The tool includes reusable Python functions that:

Load raw CSV data

Clean column names and fix data types

Detect missing or invalid values

✔ Financial Summaries

Functions generate:

Total credit (income)

Total debit (expense)

Net balance

Top spending customers

Monthly-level summaries

✔ Outlier Detection

Identifies unusually high or low transactions using the Interquartile Range (IQR) method.

✔ Visualizations (Phase 5)

The visualization.py module provides:

Monthly credit vs debit trend line

Top customers spending bar chart

Boxplot showing amount distribution and outliers

These can be shown on-screen and optionally saved into a figures/ folder.

Agile Documentation

Team_Charter.md – Team mission, working agreements, and roles.

Liftoff_Notes.md – Planning notes and early decisions.

Definition_of_Done.md – Criteria for completed features and tasks.

Branching & Collaboration Workflow

Each developer works on their own branch:

abhi-dev

bibal-dev

devarsh-dev

yash-dev

Features are added through Pull Requests.

Code is reviewed before merging.

The main branch always contains stable, production-ready work.

Commits are linked to stories/tasks in Taiga.

How to Run the Project Locally
1. Install required libraries
pip install pandas matplotlib numpy

2. Run the analysis

In the project root directory:

python main.py


This will:

Print summary tables to the console

Display all visual charts

Save figures to:

figures/

Example: Running a Single Function
from src.transactions_tool import read_data, clean_data, summarize_income_expenses

df = read_data("data/financial_transactions.csv")
df = clean_data(df)
print(summarize_income_expenses(df))

Tools & Technologies

Python 3.x

Git & GitHub

Taiga Project Management

Matplotlib

Pandas & NumPy

License

This repository was created for academic purposes as part of the
CPSC-620 Agile Software Development course at the University of Niagara Falls Canada.
