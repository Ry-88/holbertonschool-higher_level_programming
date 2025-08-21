from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]

    if username == users:
        return jsonify({"error": "Username already exists"}), 400
    
    new_user = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    users[username] = new_user

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)