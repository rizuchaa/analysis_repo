# Indonesia Banking Analysis

## 📌 Project Overview
This project analyzes key banking metrics in Indonesia using API data collection, web scraping, and visualization techniques. The goal is to create an interactive **Tableau / Power BI dashboard** for strategic decision-making.

## 📊 Key Features
- **Automated Data Collection:** Scraping & API integration for real-time banking data (100 days history).
- **Data Processing & Analysis:** Python scripts for cleaning, transformation, and insights extraction.
- **Interactive Dashboards:** Tableau / Power BI visualizations for business decision-making.
- **Consulting-Style Insights:** Actionable recommendations for banking sector improvements.

## 📁 Repository Structure
```
📦 indonesia_banking_analysis
│── 📂 data                   # Raw & processed data storage
│   ├── raw/                  # Unprocessed data files
│   ├── processed/             # Cleaned & transformed data
│   ├── api_responses/         # JSON responses from APIs
│   └── README.md              # Description of data sources
│
│── 📂 notebooks               # Jupyter notebooks for analysis
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_visualization.ipynb
│   └── README.md
│
│── 📂 scripts                 # Python scripts for automation
│   ├── fetch_api_data.py       # API data collection
│   ├── scrape_data.py          # Web scraping (if needed)
│   ├── clean_transform.py      # Data cleaning & preprocessing
│   ├── generate_dashboard.py   # Export to Tableau/Power BI
│   └── README.md
│
│── 📂 dashboards              # Visualization outputs
│   ├── tableau_dashboard.twbx
│   ├── powerbi_dashboard.pbix
│   ├── screenshots/
│   └── README.md
│
│── 📂 reports                 # Summary reports & insights
│   ├── insights_presentation.pdf
│   ├── executive_summary.md
│   ├── README.md
│
│── 📂 config                  # Configuration files
│   ├── settings.json           # API keys, URLs, etc.
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables (API keys)
│   └── README.md
│
│── .gitignore                  # Ignore unnecessary files (e.g., .env, __pycache__)
│── README.md                    # Project overview, how-to guide
│── LICENSE                      # Open-source license (MIT)
```

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rizuchaa/analysis-repo.git
cd analysis_repo
```

### 2️⃣ Install Dependencies
```bash
pip install -r config/requirements.txt
```

### 3️⃣ Set Up API Keys
- Add your API keys in `config/.env` (not included in the repo for security).

### 4️⃣ Run Data Collection
```bash
python scripts/fetch_api_data.py
```

### 5️⃣ Run Web Scraping (If Needed)
```bash
python scripts/scrape_data.py
```

### 6️⃣ Generate Dashboard
```bash
python scripts/generate_dashboard.py
```

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📜 LICENSE (MIT License)
```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## ✨ Contributors
- **[Rahmah Nur Rizki]** - Analytics Engineer

## 📢 Contact
For inquiries, reach out via [LinkedIn](https://www.linkedin.com/in/rahmah-nur-rizki/) or email **rarizki3@gmail.com**.
