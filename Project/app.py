import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

# =====================
# KPI Metrics
# =====================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Orders"].sum()

print("===== Business Dashboard =====")
print(f"Total Sales : {total_sales}")
print(f"Total Profit: {total_profit}")
print(f"Total Orders: {total_orders}")

# =====================
# Dashboard
# =====================

fig = plt.figure(figsize=(12,8))

# Sales Trend
plt.subplot(2,2,1)
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Sales Trend")

# Profit Trend
plt.subplot(2,2,2)
plt.plot(df["Month"], df["Profit"], marker="o")
plt.title("Profit Trend")

# Orders Bar Chart
plt.subplot(2,2,3)
plt.bar(df["Month"], df["Orders"])
plt.title("Orders by Month")

# Profit Distribution
plt.subplot(2,2,4)
plt.pie(
    df["Profit"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
plt.title("Profit Distribution")

plt.tight_layout()

plt.savefig("dashboard.png")

plt.show()