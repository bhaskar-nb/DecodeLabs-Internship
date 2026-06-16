-- =========================================
-- Project 3: SQL Data Analysis
-- DecodeLabs Data Analytics Internship
-- Dataset: Orders
-- Database: SQLite
-- =========================================


-- Query 1: Total Number of Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- Query 2: Total Revenue
SELECT SUM(TotalPrice) AS Total_Revenue
FROM orders;

-- Query 3: Average Order Value
SELECT ROUND(AVG(TotalPrice), 2) AS Average_Order_Value
FROM orders;

-- Query 4: Revenue by Product
SELECT Product,
       SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;

-- Query 5: Quantity Sold by Product
SELECT Product,
       SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Product
ORDER BY Total_Quantity DESC;

-- Query 6: Orders by Payment Method
SELECT PaymentMethod,
       COUNT(*) AS Orders
FROM orders
GROUP BY PaymentMethod
ORDER BY Orders DESC;

-- Query 7: Referral Source Analysis
SELECT ReferralSource,
       COUNT(*) AS Customers
FROM orders
GROUP BY ReferralSource
ORDER BY Customers DESC;

-- Query 8: Order Status Distribution
SELECT OrderStatus,
       COUNT(*) AS Total
FROM orders
GROUP BY OrderStatus;

-- Query 9: Top 5 Highest Value Orders
SELECT OrderID,
       Product,
       TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 5;

-- Query 10: Average Revenue by Product
SELECT Product,
       ROUND(AVG(TotalPrice), 2) AS Average_Revenue
FROM orders
GROUP BY Product
ORDER BY Average_Revenue DESC;

-- Query 11: Coupon Code Usage
SELECT CouponCode,
       COUNT(*) AS Usage_Count
FROM orders
GROUP BY CouponCode
ORDER BY Usage_Count DESC;

-- Query 12: Monthly Revenue
SELECT SUBSTR(Date, 1, 7) AS Month,
       SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Month
ORDER BY Month;