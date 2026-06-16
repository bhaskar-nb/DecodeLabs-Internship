import pandas as pd
df = pd.read_excel('Dataset for Data Analytics.xlsx')

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("/Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Order IDs:")
print(df['OrderID'].duplicated().sum())

print("\nData Types:")
print(df.dtypes)

df["CouponCode"] = df["CouponCode"].replace("", pd.NA)
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print("\nMissing values in 'CouponCode' after filling:")
print(df['CouponCode'].isnull().sum())

df.to_excel('Cleaned_dataset.xlsx', index=False)
print("\nCleaned dataset saved successfully.")

print("\nSummary Statistics:")
print(df.describe())