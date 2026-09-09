import os
import matplotlib.pyplot as plt
import pandas as pd
file_path = r"C:\Users\hp\Desktop\exel data.xlsx"

if not os.path.exists(file_path):
    print(
        f"Error: फ़ाइल इस रास्ते पर नहीं मिली: {file_path}\nकृपया पक्का करें कि फ़ाइल का नाम 'Excel data' है और वह Desktop पर सेव है।"
    )
else:
    df = pd.read_excel(file_path)
    print("--- 1. ओरिजिनल डेटा (Data Inspection) ---")
    print(df)
    print("Excel ke column names:")
    print(df.columns.tolist())
    df.drop_duplicates(inplace=True)

    df["unit_price"] = df["unit_price"].fillna(500)
    print("\n--- Missing Values After Handling ---")
    print(df.isnull().sum())

    print("\n--- 2. साफ-सुधरा Data ---")
    print(df)

    print("\n--- 3. डेटा का गणितीय निष्कर्ष ---")
    print(df.describe())

    numerical_cols = df[["quantity", "unit_price", "sales_amount"]]

    print("\n--- 4. Correlation Matrix ---")
    print(numerical_cols.corr())

    print("\n--- 5. आउटलायर ग्राफ़ लोड हो रहा है... ---")
    plt.figure(figsize=(6, 4))
    plt.boxplot(df["sales_amount"])
    plt.title("Outlier Identification in sales amount")
    plt.ylabel("sales amount (INR)")
    plt.show()
    print("\n--- 6. Patterns and Trends ---")

    category_sales = df.groupby("category")["sales_amount"].sum()

    print("\nCategory-wise Sales:")
    print(category_sales)

    plt.figure(figsize=(8, 5))
    category_sales.plot(kind="bar")
    plt.title("Category-wise Sales Amount")
    plt.xlabel("Category")
    plt.ylabel("Total Sales Amount (INR)")
    plt.xticks(rotation=0)
    plt.show()

    location_sales = df.groupby("location")["sales_amount"].sum()

    print("\nLocation-wise Sales:")
    print(location_sales)

    plt.figure(figsize=(8, 5))
    location_sales.plot(kind="bar")
    plt.title("Location-wise Sales Amount")
    plt.xlabel("Location")
    plt.ylabel("Total Sales Amount (INR)")
    plt.xticks(rotation=0)
    plt.show()

    # --- 7. Final Insights / Conclusion ---

    print("\n--- 7. Final Insights / Conclusion ---")

    print("\n1. Category-wise Insight:")
    print("Electronics category की sales सबसे ज्यादा है: ₹1,72,500")
    print("Furniture की sales: ₹45,000")
    print("Sports की sales सबसे कम है: ₹4,000")

    print("\n2. Location-wise Insight:")
    print("Delhi में sales सबसे ज्यादा है: ₹97,500")
    print("Mumbai में sales: ₹75,000")
    print("Bangalore में sales: ₹45,000")
    print("Pune में sales सबसे कम है: ₹4,000")

    print("\n3. Correlation Insight:")
    print("Unit Price और Sales Amount के बीच strong positive correlation है: 0.840583")

    print("\n4. Data Cleaning Insight:")
    print("Data cleaning के बाद सभी columns में missing values: 0")

    print("\n5. Outlier Insight:")
    print("Sales Amount के boxplot में कोई major outlier दिखाई नहीं दिया।")

    print("\n--- EDA Task Successfully Completed ---")