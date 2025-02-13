import sqlite3
import pandas as pd
import os
import logging
from datetime import datetime

# Ensure necessary folders exist
os.makedirs("indonesia_banking_analysis/data/sqlite", exist_ok=True)

# Configure logging
log_file = "indonesia_banking_analysis/data/log/transform_data.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting data transformation for presentation...")

# Locate the latest cleaned data file
data_folder = "indonesia_banking_analysis/data/std"
files = sorted(
    [f for f in os.listdir(data_folder) if f.startswith("std_banking_metrics_") and f.endswith(".csv")],
    reverse=True
)

if not files:
    logging.error("No standardized data files found for transformation.")
    print("No standardized data files found.")
else:
    latest_file = os.path.join(data_folder, files[0])
    logging.info(f"Loading standardized data from {latest_file}")

    # Load the dataset
    df = pd.read_csv(latest_file)

    # Convert Date column to datetime (handling yearly data)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y", errors="coerce")

    # Aggregate data for easier analysis (example: yearly averages)
    df_presentation = df.groupby(["Date", "Indicator"]).agg({"Value": "mean"}).reset_index()

    # Save to SQLite
    db_path = "indonesia_banking_analysis/data/presentation/factless_banking_analysis.db"
    conn = sqlite3.connect(db_path)

    # Store transformed data in a "factless_banking_metrics" table
    df_presentation.to_sql("factless_banking_metrics", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    logging.info(f"Transformed data stored in SQLite at {db_path}")
    print(f"Transformed data stored in SQLite at {db_path}")