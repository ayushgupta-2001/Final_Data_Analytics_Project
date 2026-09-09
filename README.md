# Executive Sales Performance Dashboard - Capstone Project

## Project Overview
This project presents a comprehensive Data Analytics lifecycle focused on a real-world Retail Sales dataset. The objective is to engineer a dynamic Power BI Dashboard to track revenue, identify premium location trends, and optimize category performance.

## Problem Statement
The business required clear visibility into sales metrics, category-wise performance, and location-based contributions to eliminate inefficiencies in underperforming regions and categories (like Sports & Furniture).

## Dataset Description
- **Source:** `exel data.xlsx`
- **Rows:** 5 Active clean transaction records.
- **Key Fields:** Transaction_ID, Product_Name, Category, Quantity, Unit Price, Sales_Amount, Location.

## Tools Used
- **Data Cleaning & Visualization:** Power BI Desktop (Power Query Engine)
- **Exploratory Data Analysis (EDA):** Python (Pandas & Matplotlib)
- **Version Control:** Git & GitHub

## Data Cleaning Process
- Handled missing data by mathematically replacing `null` values in the 'Unit Price' column with `500`.
- Eliminated redundant duplicate entries for transaction IDs to ensure 100% data integrity.

## Exploratory Data Analysis (EDA)
Performed Descriptive Statistics and Correlation Analysis in Python. A strong positive correlation of **0.84** was discovered between Product Unit Price and Sales Amount, proving high-value items dominate revenues. Boxplot analysis successfully isolated the outliers (Laptop at 90K and Smartphone at 75K).

## Key Insights & Business Recommendations
1. **Electronics Dominance:** The Electronics category generates over 75% of the total revenue.
2. **Geographical Focus:** Delhi and Mumbai are high-tier market leaders driving major sales volume.
3. **Recommendation:** Shift 70% of the active marketing budget to high-tier regions (Delhi/Mumbai) for Electronics, while testing combo deals to uplift underperforming segments like Pune and Sports.

## Conclusion
The successfully completed workflow showcases clean data handling, exploratory coding, interactive dashboard metrics, and secure Git deployment.
