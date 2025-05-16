
# Payment Tracking API

A simple RESTful API built using Flask and MySQL for managing users and tracking their payments.

##  Features

- Create, update, list, and delete users
- Record and retrieve user payments
- Organized structure using Flask
- MySQL as the database backend

##  Project Structure

```
.
├── app.py              # Main Flask application with route handlers
├── config.py           # Database configuration
├── db.py               # Database connection helper
├── models.py           # Database table creation
├── requirements.txt    # Python dependencies
```

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/payment-tracking-api.git
cd payment-tracking-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database

- Create a MySQL database named `payments_db` (or update the name in `config.py`).
- Run the table creation script:

```bash
python -c "import models; models.create_tables()"
```

### 4. Run the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`.

## 🛠 API Endpoints

###  User APIs

- **Create User**  
  `POST /users`  
  Body:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9147451517",
    "country": "IN"
  }
  ```

- **List Users**  
  `GET /users`

- **Update User**  
  `PUT /users/<user_id>`  
  Body: same as Create User

- **Delete User**  
  `DELETE /users/<user_id>`

###  Payment APIs

- **Add Payment**  
  `POST /users/<user_id>/payments`  
  Body:
  ```json
  {
    "amount": 100.50,
    "currency": "USD",
    "description": "Test payment",
    "card_no": "4111111111111111",
    "card_expiry": "12/2025",
    "card_cvc": "001"
  }
  ```

- **Get Payments for a User**  
  `GET /users/<user_id>/payments`


##  Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python`
- `Flask`

