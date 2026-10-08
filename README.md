# Financial Transactions Analytics

Python tool that turns raw financial transaction data into clear business insight: income/expense summaries, top spending categories, monthly trends, and unusual transaction flags.

## Features

- Load financial transaction data from CSV
- Clean and prepare data (handle missing values, standardize formats)
- Income vs. expense summaries
- Top spending categories
- Monthly spending trends
- Flag unusual transactions

## How to Run

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Place your dataset in `data/` as `financial_transactions.csv`.
4. Run the analysis: `python main.py`

Or use the functions directly:

```python
from src.transactions_tool import read_data, clean_data, summarize_income_expenses

df = read_data("data/financial_transactions.csv")
df_clean = clean_data(df)
summary = summarize_income_expenses(df_clean)
```

## Project Structure

- `data/` — financial transaction dataset (CSV)
- `src/transactions_tool.py` — data loading, cleaning, and analysis functions
- `tests/` — unit tests
- `main.py` — entry point script
- `requirements.txt` — Python dependencies (pandas, numpy, matplotlib)
- `LICENSE` — MIT License

## License

MIT — see LICENSE file.
