import mysql.connector

# Connect to the MySQL database (update if your service name or password is different)
conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",  # replace with your real root password
    database="products_db"
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2) NOT NULL
    )
""")

# Insert sample data
cursor.execute("INSERT INTO products (name, price) VALUES ('Bag A', 999.99)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Bag B', 499.50)")

conn.commit()
print("✅ Product database seeded.")

cursor.close()
conn.close()
