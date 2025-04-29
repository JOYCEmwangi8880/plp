# Question 1
# Write an SQL query to show the total payment amount for each payment date from payments table.
query1 = """
USE salesDB;
SELECT paymentDate, SUM(amount) AS totalamount
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;
"""

# Question 2
# Write an SQL query to find the average credit limit of each customer from customers table.
query2 = """
SELECT customerName, country, AVG(creditLimit) AS avg_credit_limit
FROM customers
GROUP BY customerName, country;
"""

# Question 3
# Write an SQL query to find the total price of products ordered from orderdetails table.
query3 = """
SELECT productCode, quantityOrdered, SUM(priceEach * quantityOrdered) AS total_price
FROM orderdetails
GROUP BY productCode, quantityOrdered;
"""

# Question 4
# Write an SQL query to find the highest payment amount for each check number from payments table.
query4 = """
SELECT checkNumber, MAX(amount) AS highest_amount
FROM payments
GROUP BY checkNumber;
"""