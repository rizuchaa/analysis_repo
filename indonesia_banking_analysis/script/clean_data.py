import pandas as pd
import os
import logging
from datetime import date

# Ensure necessary folders exist
os.makedirs("indonesia_banking_analysis/data/std", exist_ok=True)

# Configure logging
log_file = "indonesia_banking_analysis/data/log/clean_data.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting data cleaning process...")

# Locate the latest raw data file
data_folder = "indonesia_banking_analysis/data/raw"
files = sorted(
    [f for f in os.listdir(data_folder) if f.startswith("raw_banking_metrics_") and f.endswith(".csv")],
    reverse=True
)

if not files:
    logging.error("No raw data files found for cleaning.")
    print("No raw data files found.")
else:
    latest_file = os.path.join(data_folder, files[0])
    logging.info(f"Loading raw data from {latest_file}")

    # Load the dataset
    df = pd.read_csv(latest_file)

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert Value column to numeric
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

    # Drop rows with missing values
    df_cleaned = df.dropna()

    # Check if data exists after cleaning
    if df_cleaned.empty:
        logging.warning("Cleaned dataset is empty after removing missing values.")
        print("Warning: Cleaned dataset is empty.")
    else:
        # Save the cleaned dataset
        today = date.today().strftime('%Y-%m-%d')
        cleaned_filename = f"indonesia_banking_analysis/data/std/std_banking_metrics_{today}.csv"
        df_cleaned.to_csv(cleaned_filename, index=False)

        logging.info(f"Cleaned data saved to {cleaned_filename}")
        print(f"Cleaned data saved to {cleaned_filename}")
