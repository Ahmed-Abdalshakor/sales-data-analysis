import pandas as pd

# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Basic sales metrics
total_sales = df["Total_Sales"].sum()
total_orders = len(df)
total_units = df["Quantity"].sum()
average_order_value = df["Total_Sales"].mean()

# Best-selling product by revenue
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
best_product = product_sales.index[0]

# Best month by revenue
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total_Sales"].sum().sort_values(ascending=False)
best_month = monthly_sales.index[0]

# Save summary
summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Orders",
        "Total Units Sold",
        "Average Order Value",
        "Best Product by Revenue",
        "Best Month by Revenue"
    ],
    "Value": [
        total_sales,
        total_orders,
        total_units,
        round(average_order_value, 2),
        best_product,
        str(best_month)
    ]
})

summary.to_csv("sales_summary.csv", index=False)

print("=== Sales Analysis ===")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Units Sold: {total_units}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Best Product by Revenue: {best_product}")
print(f"Best Month by Revenue: {best_month}")
print("\nSummary saved to sales_summary.csv")
