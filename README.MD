# Olist ETL Pipeline

## What this does
Extracts raw e-commerce order data from the Olist Kaggle dataset, validates and 
cleans it, and loads the result into a local PostgreSQL database.

## Stack
- Python 3.x
- pandas
- SQLAlchemy
- psycopg2
- PostgreSQL

## How to run

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
2. Place `olist_orders_dataset.csv` and `olist_order_items_dataset.csv` in `data/raw/`
3. Create a PostgreSQL database called `olist_db`
4. Update the connection string in `etl_pipeline.py`
5. Install dependencies: `pip install -r requirements.txt`
6. Run: `python etl_pipeline.py`

## Output
- `clean_orders` table in PostgreSQL with validated, normalized order data
- `output/rejected_rows.csv` with rows that failed validation and their rejection reasons