import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_data():
    df1 = pd.read_csv(r'data\raw\olist_order_items_dataset.csv')
    df2 = pd.read_csv(r'data\raw\olist_orders_dataset.csv')
    total_rows = len(df1) + len(df2)
    logger.info(f"Extracted {len(df1)} order items and {len(df2)} orders (total: {total_rows} rows)")
    return df1, df2

def transform_data(df1, df2):
    # 1. Merge first
    merged_df = pd.merge(df1, df2, on='order_id', how='left')
    
    # 2. Filter out canceled and unavailable rows
    filtered_df = merged_df[~merged_df['order_status'].isin(['canceled', 'unavailable'])]
    
    # 3. Run price validation - separate clean and rejected rows
    invalid_rows = filtered_df[(filtered_df['price'].isna()) | (filtered_df['price'] < 0)].copy()
    invalid_rows['rejection_reason'] = invalid_rows['price'].apply(
        lambda x: 'missing price' if pd.isna(x) else 'price must be greater than zero'
    )
    invalid_rows.to_csv(r'output\rejected_rows.csv', index=False)
    rejected_count = len(invalid_rows)
    
    # Keep only valid rows
    valid_rows = filtered_df[~((filtered_df['price'].isna()) | (filtered_df['price'] < 0))].copy()
    
    # 4. Normalize timestamps on clean rows only
    cols = ["order_purchase_timestamp", "order_approved_at", "order_delivered_customer_date"]
    for c in cols:
        valid_rows[c] = pd.to_datetime(valid_rows[c], errors="coerce")
    
    # Handle NaT in order_approved_at
    valid_rows["order_approved_at"] = valid_rows["order_approved_at"].dt.strftime("%Y-%m-%d %H:%M:%S")
    valid_rows.loc[valid_rows["order_approved_at"].isna(), "order_approved_at"] = "NOT_APPROVED"
    
    # Convert other timestamps to string format
    valid_rows["order_purchase_timestamp"] = valid_rows["order_purchase_timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
    valid_rows["order_delivered_customer_date"] = valid_rows["order_delivered_customer_date"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    # 5. Add order_year_month last (after timestamps are clean)
    valid_rows["order_year_month"] = pd.to_datetime(valid_rows["order_purchase_timestamp"], errors="coerce").dt.strftime("%Y-%m")
    
    logger.info(f"Transform complete: {len(valid_rows)} clean rows, {rejected_count} rejected rows")
    return valid_rows, rejected_count

def load_data(df):
    """Load clean data to CSV output."""
    output_path = r'output\clean_orders.csv'
    df.to_csv(output_path, index=False)
    logger.info(f"Loaded {len(df)} rows into '{output_path}'")

def main():
    """Main ETL pipeline orchestration."""
    df1, df2 = extract_data()
    clean_data, rejected_count = transform_data(df1, df2)
    load_data(clean_data)

if __name__ == '__main__':
    main()