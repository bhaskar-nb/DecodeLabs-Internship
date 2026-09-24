# DecodeLabs Data Analytics Internship

A practical **end-to-end data analytics internship project** covering data cleaning, exploratory data analysis, SQL business analysis, and Tableau dashboard development.

The repository shows how the same order dataset was taken through multiple stages:

**raw data → cleaning → EDA → SQL analysis → dashboard reporting**

## Internship Projects

### 1. Data Cleaning

Python and Pandas were used to inspect and prepare the source data.

Key work:
- Checked missing values and duplicate records
- Checked duplicate `OrderID` values
- Reviewed data types and summary statistics
- Replaced blank `CouponCode` values with `No Coupon`
- Exported a cleaned Excel dataset for downstream analysis

**Tools:** Python · Pandas · OpenPyXL

### 2. Exploratory Data Analysis

EDA was used to understand business patterns and data quality before reporting.

Analysis includes:
- Revenue and order-value statistics
- Product revenue and quantity analysis
- Payment-method distribution
- Referral-source analysis
- Monthly revenue trends
- Order-status analysis
- Outlier analysis using IQR
- Correlation analysis
- Coupon-code usage

**Tools:** Python · Pandas · Matplotlib

Supporting outputs include revenue, payment, referral, order-status, outlier, correlation, and monthly-trend visualizations.

### 3. SQL Business Analysis

The cleaned dataset was loaded into **SQLite** and analyzed with SQL.

The repository contains 12 business-oriented queries covering:

- Total orders
- Total revenue
- Average order value
- Revenue by product
- Quantity sold by product
- Orders by payment method
- Referral-source volume
- Order-status distribution
- Top 5 highest-value orders
- Average revenue by product
- Coupon-code usage
- Monthly revenue

**Tools:** SQL · SQLite · DB Browser for SQLite

### 4. Tableau Sales Dashboard

The analysis was converted into an interactive Tableau dashboard using the cleaned dataset.

Dashboard views include:
- Revenue by product
- Monthly revenue trend
- Order-status analysis
- Payment-method analysis
- Referral-source analysis

The Tableau workbook is available at `Project_4_Tableau/Sales_Performance_Dashboard.twb`, with a dashboard preview in `Project_4_Tableau/dashboard.png`.

## Key Findings

The documented Tableau analysis identifies:

- **Chair** as the highest-revenue product
- **Online** as the most frequently used payment method
- **Instagram** as the referral source with the highest recorded customer count
- Variation in revenue across months
- Order-status differences that provide additional operational context

These findings describe the dataset used for the internship projects and should not be interpreted as current business performance.

## End-to-End Workflow

```text
Source Order Dataset
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
SQL Business Analysis
        ↓
Tableau Dashboard
        ↓
Business Reporting
```

## Repository Structure

```text
DecodeLabs-Internship/
├── Project_1_Data_Cleaning/
│   ├── Dataset for Data Analytics.xlsx
│   ├── Cleaned_dataset.xlsx
│   └── data_cleaning.py
│
├── Project_2_EDA/
│   ├── Cleaned_dataset.xlsx
│   ├── exploratory_analysis.py
│   ├── EDA report.docx
│   └── analysis output images
│
├── Project_3_SQL/
│   ├── Cleaned_dataset.csv
│   ├── orders.db
│   └── SQL_Queries.sql
│
├── Project_4_Tableau/
│   ├── Cleaned_dataset.csv
│   ├── Sales_Performance_Dashboard.twb
│   └── dashboard.png
│
└── README.md
```

## Skills Demonstrated

- Data cleaning and preparation
- Exploratory data analysis
- Python and Pandas
- SQL and SQLite
- Business KPI analysis
- Aggregation and grouping
- Time-based analysis
- Outlier analysis
- Correlation analysis
- Data visualization
- Tableau dashboard development
- Business insight communication
- End-to-end analytics workflow

## Technologies

| Area | Tools |
|---|---|
| Programming | Python |
| Data analysis | Pandas, NumPy |
| Excel processing | OpenPyXL |
| Visualization | Matplotlib, Tableau |
| SQL | SQLite, DB Browser for SQLite |
| Version control | Git, GitHub |

## Internship Scope

This repository documents work completed during the **DecodeLabs Data Analytics Internship**.

The projects are portfolio and learning work based on the supplied dataset; they are not presented as production analytics systems.

## Notes

Project 1 and Project 2 use Excel files during the preparation/EDA workflow, while Project 3 and Project 4 use the cleaned CSV output. This keeps the repository traceable from data preparation through reporting.

## Author

**Bhaskar Nakka**  
Data Analyst | SQL · Python · Excel · Tableau · Power BI