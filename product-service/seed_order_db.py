import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",
    database="orders_db"
)

cursor = connection.cursor()

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    total_price FLOAT
)
""")

# Insert dummy order
cursor.execute("""
INSERT INTO orders (product_id, quantity, total_price)
VALUES (1, 2, 39.98)
""")

connection.commit()
cursor.close()
connection.close()

print("✅ Orders database seeded successfully.")
