from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL DB connection setup
db_config = {
    'host': os.environ.get('MYSQL_HOST', 'mysql'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', 'password'),
    'database': os.environ.get('MYSQL_DB', 'ecommerce')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT o.id, o.product_id, o.quantity, p.name, p.price
        FROM orders o
        JOIN products p ON o.product_id = p.id
    """)
    orders = cursor.fetchall()
    conn.close()
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({'error': 'Missing product_id or quantity'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (product_id, quantity) VALUES (%s, %s)", (product_id, quantity))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order placed'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
