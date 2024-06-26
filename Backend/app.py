from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Products list
products = [
    
    {
    "id": 1,
    "name": "Product 1",
    "description": "Description for Product 1",
    "price": 10.99,
    "image": 'images/product1.png'
    },
    {
    "id": 2,
    "name": "Product 2",
    "description": "Description for Product 2",
    "price": 20.99,
    "image": 'images/product2.jpg'
    },
    {
    "id": 3,
    "name": "Product 3",
    "description": "Description for Product 3",
    "price": 10.99,
    "image": 'images/product3.jpg'
    },
    {
    "id": 4,
    "name": "Product 4",
    "description": "Description for Product 4",
    "price": 10.99,
    "image": 'images/product4.jpg'
    },
    {
    "id": 5,
    "name": "Product 5",
    "description": "Description for Product 5",
    "price": 10.99,
    "image": 'images/product5.jpg'
    },
    {
    "id": 6,
    "name": "Product 6",
    "description": "Description for Product 6",
    "price": 10.99,
    "image": 'images/product6.jpg'
    },
    {
    "id": 7,
    "name": "Product 7",
    "description": "Description for Product 7",
    "price": 10.99,
    "image": 'images/product7.jpg'
    },
    {
    "id": 8,
    "name": "Product 8",
    "description": "Description for Product 8",
    "price": 10.99,
    "image": 'images/product8.jpg'
    },
    {
    "id": 9,
    "name": "Product 9",
    "description": "Description for Product 9",
    "price": 10.99,
    "image": 'images/product9.jpg'
    },
    {
    "id": 10,
    "name": "Product 10",
    "description": "Description for Product 10",
    "price": 10.99,
    "image": 'images/product10.jpg'
    }
]


# Helper Functions
def load_users():
    global users
    try:
        with open("users.json", 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)


# load uses.json file before signup and login so we have the user's list ready
load_users()

@app.route("/signup", methods=["POST"])
def sign_up():
    global users
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    # Check to ensure the fields aren't empty
    if not username or not password or not email:
        return jsonify({"error": "Username, password, and email are required"}), 400
    
    # check to ensure username doesn't already exist
    if any(user["username"] == username for user in users):
        return jsonify({"error": "Username already exists"}), 400
    
    new_user = {
        "username": username,
        "password": password,
        "email": email
    }

    users.append(new_user)
    save_users()
    return jsonify({"message": "User created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    global users
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check to ensure the fields aren't empty
    if not username or not password:
        return jsonify({"error": "Username, password, and email are required"}), 400
    
    matched_users = [user for user in users if user["username"] == username]

    if not matched_users:
        return jsonify({"error": "User not found"}), 404

    # this assumes that usernames are unique 
    matched_user = matched_users[0]
    if matched_user["password"] != password:
        return jsonify({"error": "Incorrect password"}), 401
    
    return jsonify({"message": "Login successful"}), 200

@app.route ('/products', methods =['GET'])
def get_products():
    return jsonify({"products": products})


if __name__ == "__main__":
    app.run(debug=True)