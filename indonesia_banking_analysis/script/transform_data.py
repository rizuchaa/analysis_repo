import pandas as pd
import os
import logging
from datetime import datetime

# Ensure necessary folders exist
os.makedirs("indonesia_banking_analysis/data/presentation", exist_ok=True)

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

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Aggregate data for Tableau presentation (example: Monthly averages)
    df_presentation = df.groupby([df["Date"].dt.to_period("M"), "Indicator"]).agg({"Value": "mean"}).reset_index()
    df_presentation["Date"] = df_presentation["Date"].astype(str)  # Convert period to string

    # Save the transformed dataset
    date_str = datetime.today().strftime("%Y-%m-%d")
    transformed_filename = f"indonesia_banking_analysis/data/presentation/factless_banking_metrics_{date_str}.csv"
    df_presentation.to_csv(transformed_filename, index=False)

    logging.info(f"Transformed data saved to {transformed_filename}")
    print(f"Transformed data saved to {transformed_filename}")