# app.py
from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone, country) VALUES (%s, %s, %s, %s)",
                   (data['name'], data['email'], data['phone'], data['country']))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'id': user_id}), 201

# List all users
@app.route('/users', methods=['GET'])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s, phone=%s, country=%s WHERE id=%s",
                   (data['name'], data['email'], data['phone'], data['country'], user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

# Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

# Add payment
@app.route('/users/<int:user_id>/payments', methods=['POST'])
def add_payment(user_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO payments 
        (user_id, amount, currency, description, card_no, card_expiry, card_cvc)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (user_id, data['amount'], data['currency'], data['description'],
         data['card_no'], data['card_expiry'], data['card_cvc']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Payment added'}), 201

# Get all payments for a user
@app.route('/users/<int:user_id>/payments', methods=['GET'])
def get_payments(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments WHERE user_id=%s", (user_id,))
    payments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(payments)

if __name__ == '__main__':
    app.run(debug=True)
