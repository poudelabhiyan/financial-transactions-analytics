# Assignment 2 – Financial Transactions Summary Tool

### Course: CPSC-620 (Version Control & Agile Collaboration)
### Team Members:
- Abhiyan Poudel  
- Bibal Adhikari  
- Devarsh Ketankumar Oza  
- Yash Milankumar Patel  

---

## **Project Overview**
The Financial Transactions Summary Tool is a modular Python-based application designed to analyze a dataset of financial transactions.  
It reads transaction records from a CSV file, processes the data, and provides summaries such as total income, total expenses, and category-wise spending.  
This project follows Agile principles and version control best practices to promote collaboration and transparency.

---

## **Key Objectives**
- Practice Agile teamwork using GitHub and Taiga.  
- Apply version control concepts (branching, pull requests, code reviews).  
- Develop clean, modular, and well-documented Python code.  
- Deliver traceable documentation including a Team Charter, Liftoff Notes, and Definition of Done.

---

## **Repository Structure**
Assignment2_FinancialTransactions/
│
├── docs/
│ ├── Team_Charter.md
│ ├── Liftoff_Notes.md
│ └── Definition_of_Done.md
│
├── src/
│ ├── record.py
│ ├── converter.py
│ └── analytics.py
│
├── .gitignore
└── README.md


---

## **Agile Documentation**
- **Team_Charter.md:** Defines mission, roles, working agreements, and responsibilities.  
- **Liftoff_Notes.md:** Records key meeting outcomes and planning decisions.  
- **Definition_of_Done.md:** Lists completion criteria for all deliverables.

---

## **Collaboration Workflow**
1. Each team member works on their own branch (`abhi-dev`, `bibal-dev`, `devarsh-dev`, `yash-dev`).  
2. All changes are merged through pull requests with reviews.  
3. Every commit message links to a task or story in Taiga.  
4. The main branch always holds production-ready code.

---

## **Tools & Technologies**
- **Programming:** Python 3.x  
- **Version Control:** Git & GitHub  
- **Project Management:** Taiga  
- **Collaboration:** Microsoft Teams & WhatsApp  

---

## **License**
This repository is created for educational purposes as part of the CPSC-620 Agile coursework at the University of Niagara Falls Canada.

Project structure
src/  Python module with reusable functions
data/ financial_transactions.csv
tests/ basic tests
transactions_tool_demo.ipynb  notebook to run and view visuals

How to run locally
pip install -r requirements.txt
python - <<EOF
from src.transactions_tool import read_data, clean_data, summarize_income_expenses
df = read_data("data/financial_transactions.csv")
df = clean_data(df)
print(summarize_income_expenses(df))
EOF
