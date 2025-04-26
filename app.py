from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import uuid
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)  # Initialize Flask-Bcrypt

# MongoDB connection
client = MongoClient('mongodb+srv://hajrazawwarmalik:7KnkNxNRfuHxttSa@instagramlitecluster.tlxvfb7.mongodb.net/?retryWrites=true&w=majority&appName=InstagramLiteCluster')
db = client['instagram_lite']
users_collection = db['users']
posts_collection = db['posts']

# Registration API (add this)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = {
        "_id": str(uuid.uuid4()),
        "email": data['email'],
        "password": hashed_password  # Store the hashed password
    }
    users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully!"}), 201


# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users_collection.find_one({"email": data['email']})
    if user and bcrypt.check_password_hash(user['password'], data['password']): # Verify password
        return jsonify({"message": "Login Successful", "user_id": str(user['_id'])}), 200
    else:
        return jsonify({"message": "Invalid Credentials"}), 401

# Upload Post API
@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    post = {
        "_id": str(uuid.uuid4()),
        "user_id": data['user_id'],
        "caption": data['caption'],
        "media_url": data['media_url'],
        "created_at": datetime.utcnow(),
        "likes": 0,
        "comments": []
    }
    posts_collection.insert_one(post)
    return jsonify({"message": "Post uploaded successfully!"}), 201

# Get Feed API
@app.route('/feed', methods=['GET'])
def feed():
    posts = list(posts_collection.find({}).sort("created_at", -1))
    for post in posts:
        post['_id'] = str(post['_id'])
    return jsonify(posts), 200

if __name__ == "__main__":
    app.run(debug=True)