Sprint Planning and User Stories — Assignment 2: Financial Transactions Summary Tool

Date: November 13, 2025
Sprint Duration: 1 week
Team Members: Abhiyan Poudel, Bibal Adhikari, Devarsh Ketankumar Oza, Yash Milankumar Patel

Sprint Goal

To build a working Python tool that can load, clean, and summarize the financial transactions dataset. The tool should provide clear insights such as total income, total expenses, top spending categories, monthly summaries, and unusual transactions. All work should follow Agile practices and show proper use of GitHub and Taiga.

Sprint Overview

During this sprint, the team planned the work using Taiga, broke down the project into user stories, and assigned each story to a team member. Each user story has acceptance criteria, tasks, and a feature branch linked to it.
The sprint focuses on delivering a simple but functional version of the tool with clean code, readable outputs, and good collaboration.

User Stories

Below are the six user stories planned for the sprint.
Each story follows the format: As a user, I want… so that…

US1 — Read and Load the Dataset

Story:
As a user, I want the program to load the financial transactions file so that I can work with the data inside Python.

Acceptance Criteria:

The CSV file loads without errors.

The dataset appears with correct columns.

Invalid file paths show a clear error message.

Output is a clean DataFrame ready for further steps.

Assigned To: Yash
Branch: feature/US1-read-data

US2 — Clean and Prepare the Data

Story:
As a user, I want the dataset to be cleaned and prepared so that I can analyze it without issues.

Acceptance Criteria:

Column names are consistent.

Missing or invalid values are handled.

Amounts and dates are converted to proper data types.

Cleaned output is ready for analysis.

Assigned To: Devarsh
Branch: feature/US2-clean-data

US3 — Income and Expense Summary

Story:
As a user, I want a summary of total income, total expenses, and net balance so that I can quickly see my financial overview.

Acceptance Criteria:

Income (positive amounts) is summed correctly.

Expenses (negative amounts) are summed correctly.

Net total is calculated.

Output is clear and easy to understand.

Assigned To: Abhiyan
Branch: feature/US3-income-expense-summary

US4 — Top Expense Categories

Story:
As a user, I want to see my top spending categories so that I know where most of my money goes.

Acceptance Criteria:

Categories are grouped and sorted by expense amount.

The top 5 categories are shown.

Results are formatted clearly.

Works even if some categories have missing values.

Assigned To: Bibal
Branch: feature/US4-top-categories

US5 — Monthly Summary

Story:
As a user, I want a month-by-month breakdown of income and expenses so that I can understand trends over time.

Acceptance Criteria:

Transactions are grouped by month.

Monthly income, expenses, and net totals are shown.

Dates are handled correctly.

Output is easy to read.

Assigned To: Abhiyan
Branch: feature/US5-monthly-summary

US6 — Detect Unusual Transactions

Story:
As a user, I want unusual or suspicious transactions to be highlighted so that I can review them manually.

Acceptance Criteria:

Unusual transactions are detected using a simple logical rule (example: very high amounts).

Output clearly lists unusual entries.

Method handles unexpected values safely.

User can understand why a transaction is marked unusual.

Assigned To: Abhiyan
Branch: feature/US6-unusual-transactions

Task Breakdown

Each user story has the following tasks:

Review the dataset and understand required fields

Create or update the function for the story

Test the output

Commit changes with a clear message referencing the US number

Push changes to the feature branch

Open a Pull Request for review

Move the task through Taiga: New → In Progress → Testing → Done

Sprint Planning Outcome

By the end of planning, the team completed:

A clear sprint goal

Six user stories with acceptance criteria

Story assignments for every team member

Feature branch creation for all stories

Task creation and placement in Taiga

Agreement on workflow, communication, and review processes

Planning is complete, and the team has moved into development.
