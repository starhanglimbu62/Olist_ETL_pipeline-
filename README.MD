# 🗄️ Olist ETL Pipeline

<p align="center">
  A Python ETL pipeline that extracts, validates, and loads Brazilian e-commerce order data from Kaggle into a structured PostgreSQL database.
</p>

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

---

## ✨ Key Features

- Extracts raw order data from the Olist Kaggle dataset automatically
- Validates and cleans records before any data reaches the database
- Loads normalized data into a structured PostgreSQL `clean_orders` table
- Exports rejected rows with labeled rejection reasons to CSV
- Separates raw input from clean output via a defined folder structure

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- A running PostgreSQL instance
- A [Kaggle account](https://www.kaggle.com) to download the dataset

### Installation & Run

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

2. Place the required files into the `data/raw/` directory:

```text
data/raw/olist_orders_dataset.csv
data/raw/olist_order_items_dataset.csv
```

3. Create the target PostgreSQL database:

```sql
CREATE DATABASE olist_db;
```

4. Update the database connection string inside `etl_pipeline.py`:

```python
# etl_pipeline.py
CONNECTION_STRING = "postgresql+psycopg2://user:password@localhost/olist_db"
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the pipeline:

```bash
python etl_pipeline.py
```

---

## 📁 Project Structure

```text
olist-etl-pipeline/
├── data/
│   └── raw/
│       ├── olist_orders_dataset.csv
│       └── olist_order_items_dataset.csv
├── output/
│   └── rejected_rows.csv
├── etl_pipeline.py
└── requirements.txt
```

---

## 📤 Output

| Output | Location | Description |
|--------|----------|-------------|
| Clean orders table | PostgreSQL: `clean_orders` | Validated, normalized order data |
| Rejected rows log | `output/rejected_rows.csv` | Rows that failed validation with rejection reasons |

---

## 📸 Screenshots / Demo

<!-- Add screenshots here -->

---

## 💡 Motivation

I built this project to practice designing a complete, production-style ETL pipeline from raw data ingestion through validation and storage. Working with a real-world e-commerce dataset gave me hands-on experience with data quality issues and the importance of isolating rejected records for auditability rather than silently dropping them.

---

## 📬 Contact / Connect

Starhang Limbu(https://github.com/starhanglimbu62)
