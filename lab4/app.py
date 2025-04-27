from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"admin": "password123"}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if users.get(username) == password:
        return jsonify({"message": "Login successful", "token": "securetoken123"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get('Authorization')
    if token == "Bearer securetoken123":
        return jsonify({"username": "admin", "email": "admin@example.com"})
    else:
        return jsonify({"message": "Unauthorized"}), 403

if __name__ == '__main__':
    app.run(debug=True)
