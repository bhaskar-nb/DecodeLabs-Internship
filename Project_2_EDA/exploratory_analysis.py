import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
    return pd.read_excel("Cleaned_dataset.xlsx")
def dataset_overview(df):
    print("\n" + "=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nDataset Info:")
    df.info()

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

def business_statistics(df):
    print("\n" + "=" * 50)
    print("BUSINESS STATISTICS")
    print("=" * 50)

    print(f"Total Revenue: {df['TotalPrice'].sum():.2f}")
    print(f"Average Order Value: {df['TotalPrice'].mean():.2f}")
    print(f"Median Order Value: {df['TotalPrice'].median():.2f}")
    print(f"Maximum Order Value: {df['TotalPrice'].max():.2f}")
    print(f"Minimum Order Value: {df['TotalPrice'].min():.2f}")
    print(f"Total Quantity Sold: {df['Quantity'].sum()}")
    print(f"Average Quantity Sold: {df['Quantity'].mean():.2f}")

def product_analysis(df):
    print("\n" + "=" * 50)
    print("PRODUCT ANALYSIS")
    print("=" * 50)

    product_quantity = (
        df.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    product_revenue = (
        df.groupby("Product")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nQuantity Sold by Product:")
    print(product_quantity)

    print("\nRevenue by Product:")
    print(product_revenue)

    product_revenue.plot(kind="bar", figsize=(10, 6))
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("revenue_by_product.png")
    plt.show()

def payment_analysis(df):
    print("\n" + "=" * 50)
    print("PAYMENT METHOD ANALYSIS")
    print("=" * 50)

    payment_counts = df["PaymentMethod"].value_counts()

    print(payment_counts)

    payment_counts.plot(kind="bar", figsize=(8, 5))
    plt.title("Orders by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig("payment_method_distribution.png")
    plt.show()

def referral_analysis(df):
    print("\n" + "=" * 50)
    print("REFERRAL SOURCE ANALYSIS")
    print("=" * 50)

    referral_counts = df["ReferralSource"].value_counts()

    print(referral_counts)

    referral_counts.plot(kind="bar", figsize=(8, 5))
    plt.title("Customers by Referral Source")
    plt.xlabel("Referral Source")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig("referral_source.png")
    plt.show()

def monthly_revenue_analysis(df):
    print("\n" + "=" * 50)
    print("MONTHLY REVENUE ANALYSIS")
    print("=" * 50)

    df["YearMonth"] = df["Date"].dt.strftime("%Y-%m")

    monthly_revenue = (
        df.groupby("YearMonth")["TotalPrice"]
        .sum()
    )

    print(monthly_revenue)

    monthly_revenue.plot(
        kind="line",
        marker="o",
        figsize=(12, 6)
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_revenue.png")
    plt.show()

def outlier_analysis(df):
    print("\n" + "=" * 50)
    print("OUTLIER ANALYSIS")
    print("=" * 50)

    Q1 = df["TotalPrice"].quantile(0.25)
    Q3 = df["TotalPrice"].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df["TotalPrice"] < lower) |
        (df["TotalPrice"] > upper)
    ]

    print(f"Q1: {Q1:.2f}")
    print(f"Q3: {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Lower Bound: {lower:.2f}")
    print(f"Upper Bound: {upper:.2f}")
    print(f"Number of Outliers: {len(outliers)}")

    plt.figure(figsize=(8, 5))
    plt.boxplot(df["TotalPrice"])
    plt.title("Box Plot of Total Price")
    plt.ylabel("Total Price")
    plt.savefig("outlier_boxplot.png")
    plt.show()

def correlation_analysis(df):
    print("\n" + "=" * 50)
    print("CORRELATION ANALYSIS")
    print("=" * 50)

    numeric_data = df[
        ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
    ]

    corr = numeric_data.corr()

    print(corr)

    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=45
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()

def order_status_analysis(df):
    print("\n" + "=" * 50)
    print("ORDER STATUS ANALYSIS")
    print("=" * 50)

    status_counts = df["OrderStatus"].value_counts()

    print(status_counts)

    status_counts.plot(kind="bar", figsize=(8, 5))
    plt.title("Order Status Distribution")
    plt.xlabel("Order Status")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig("order_status.png")
    plt.show()

def coupon_analysis(df):
    print("\n" + "=" * 50)
    print("COUPON CODE ANALYSIS")
    print("=" * 50)

    coupon_counts = df["CouponCode"].value_counts()

    print(coupon_counts)


def main():
    df = load_dataset()

    dataset_overview(df)
    business_statistics(df)
    product_analysis(df)
    payment_analysis(df)
    referral_analysis(df)
    monthly_revenue_analysis(df)
    outlier_analysis(df)
    correlation_analysis(df)
    order_status_analysis(df)
    coupon_analysis(df)


if __name__ == "__main__":
    main()