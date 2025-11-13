Assignment 2 – Financial Transactions Summary Tool
Course: CPSC-620 (Version Control and Agile Collaboration)
Team Members:
Abhiyan Poudel
Bibal Adhikari
Devarsh Ketankumar Oza
Yash Milankumar Patel

Project Overview
The Financial Transactions Summary Tool is a modular Python application developed to analyze a dataset of financial transactions. The tool loads a CSV file, cleans and processes the data, and generates useful insights including total income, total expenses, top spending customers, monthly financial trends, and outlier detection. This project follows Agile practices and uses GitHub for version control and collaborative development.
Key Objectives
•	Apply Agile teamwork through branching, code reviews, and pull requests.
•	Develop reusable Python functions for data loading, processing, summarizing, and visualization.
•	Produce clean, organized, and well-documented code.
•	Maintain supporting documentation including a Team Charter, Liftoff Notes, and Definition of Done.
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
│   ├── transactions_tool.py
│   └── visualization.py
│
├── tests/
│   └── .keep
│
├── main.py
├── README.md
└── .gitignore
Core Features
Data Processing
The tool includes functions that load the raw CSV file, standardize column names, correct data types, and handle missing values.
Financial Summaries
The tool provides:
•	Total credit (income)
•	Total debit (expense)
•	Net balance
•	Top spending customers
•	Monthly activity summaries
Outlier Detection
A function is included to identify unusually high or low transaction amounts using the IQR method.
Visualizations
The visualization module produces:
•	A monthly credit vs debit trend chart
•	A bar chart of top spending customers
These charts are displayed on screen and can be saved as image files.
Agile Documentation
•	Team_Charter.md outlines team roles, responsibilities, and mission.
•	Liftoff_Notes.md documents early planning and decisions.
•	Definition_of_Done.md lists the standards for completing tasks and deliverables.
Branching and Collaboration Workflow
•	Each team member works on an individual development branch.
•	Pull requests are used to merge changes into the main branch.
•	Code is reviewed before merging.
•	The main branch always contains stable and working code.
•	All commits are linked to tasks in Taiga for transparency.
Running the Project Locally
Step 1: Install dependencies
pip install pandas matplotlib numpy
Step 2: Run the main script
From the project root directory:
python main.py
This will print analysis summaries and generate all visual charts.
Images will be saved in the "figures" directory.
Example: Running Individual Functions
from src.transactions_tool import read_data, clean_data, summarize_income_expenses

df = read_data("data/financial_transactions.csv")
df = clean_data(df)
print(summarize_income_expenses(df))
Tools and Technologies
Python 3
Git and GitHub
Taiga Project Management
Matplotlib
Pandas and NumPy
License
This repository was created for academic use in the CPSC-620 Agile Software Development course at the University of Niagara Falls Canada.

