
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route("/data")
def data():
    names = [user["name"] for user in users.values()]
    return jsonify(names)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data or "name" not in data or "age" not in data or "city" not in data:
        return jsonify({"error":"Username is required"}), 400
    
    username = data["username"]

    if username in users:
        return jsonify({"error": "username alreday exists"}), 400
    
    new_user = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    users[username] = new_user

    return jsonify({"message": "user added", "user": new_user}), 201

if __name__ == "__main__": app.run(debug=True)