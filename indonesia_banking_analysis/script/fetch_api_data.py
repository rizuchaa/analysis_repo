#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
import os
import logging
from datetime import datetime

# Ensure the log folder exists
os.makedirs("indonesia_banking_analysis/data/raw", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="indonesia_banking_analysis/data/log/fetch_api_data.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting API fetch process...")

# Define the indicators to fetch
indicators = {
    "NIM": "FR.INR.LEND",  # Net Interest Margin
    "LDR": "FB.BNK.LEND.ZS",  # Loan-to-Deposit Ratio (example, check exact code)
    "NPL": "FB.AST.NPER.ZS",  # Non-Performing Loan Ratio
    "CAR": "FB.BNK.CAPA.ZS"  # Capital Adequacy Ratio
}

# Base URL for World Bank API
base_url = "https://api.worldbank.org/v2/country/ID/indicator/{}?format=json"


def fetch_indicator_data(indicator_code):
    url = base_url.format(indicator_code)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {indicator_code}: {e}")
        return None


def parse_data(indicator_name, raw_data):
    if raw_data and isinstance(raw_data, list) and len(raw_data) > 1:
        records = raw_data[1]  # Data is in the second element of the response
        return [
            {
                "Indicator": indicator_name,
                "Date": entry.get("date"),
                "Value": entry.get("value")
            }
            for entry in records if entry.get("value") is not None
        ]
    return []


# Fetch and parse data
all_data = []
for name, code in indicators.items():
    raw_data = fetch_indicator_data(code)
    if raw_data:
        parsed_data = parse_data(name, raw_data)
        all_data.extend(parsed_data)
        logging.info(f"Fetched {len(parsed_data)} records for {name}")
    else:
        logging.warning(f"No data retrieved for {name}")

# Convert to DataFrame and save
if all_data:
    df = pd.DataFrame(all_data)
    os.makedirs("indonesia_banking_analysis/data/raw", exist_ok=True)
    filename = f"indonesia_banking_analysis/data/raw/raw_banking_metrics_{datetime.today().strftime('%Y-%m-%d')}.csv"
    df.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")
    print(f"Data saved to {filename}")
else:
    logging.error("No data available to save.")
    print("No data available to save.")
