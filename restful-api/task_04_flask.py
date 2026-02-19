#!/usr/bin/env python3
"""
Simple Flask API Module.

This module implements a basic REST API to manage a user database
stored in memory using a dictionary.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated in-memory database
users = {}

@app.route('/')
def home():
    """
    API Root endpoint.

    Returns:
        str: A plain text welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Retrieve the list of all usernames.

    Returns:
        Response: A JSON object containing a list of keys from the users dictionary.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Health check endpoint.

    Returns:
        str: The message "OK" if the server is running correctly.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieve details for a specific user.

    Args:
        username (str): The unique username to look up.

    Returns:
        tuple: (JSON, int) The user data with a 200 status code,
               or an error message with a 404 status code if not found.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the database.

    Expects a JSON request body containing at least a "username" key.
    Optional keys: "name", "age", "city".

    Returns:
        tuple: (JSON, int) A success message (201), a "Missing Data" error (400),
               or a "Conflict" error (409) if the username already exists.
    """
    data = request.get_json()

    # Input validation
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check for duplicates
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # User creation
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
