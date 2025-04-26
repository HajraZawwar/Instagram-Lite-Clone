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
# GET USER PROFILE
@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = users_collection.find_one({"_id": user_id})
        if user:
            # Remove sensitive information like password hash
            user['_id'] = str(user['_id'])  # Convert ObjectId to string
            user.pop('password', None)  # Remove password field
            return jsonify(user), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        print(f"Error getting user: {e}")
        return jsonify({"message": "Failed to get user. Please try again later."}, 500)

# UPDATE USER PROFILE
@app.route('/update_profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    full_name = data.get('full_name')
    bio = data.get('bio')
    profile_picture_url = data.get('profile_picture_url')

    try:
        # Validate user_id
        if not user_id:
            return jsonify({"message": "User ID is required"}), 400

        # Basic input validation (you should add more robust validation)
        if username and len(username) > 50:
            return jsonify({"message": "Username too long"}), 400
        if bio and len(bio) > 200:
            return jsonify({"message": "Bio too long"}), 400

        # Build the update dictionary
        update_data = {}
        if username:
            update_data['username'] = username
        if full_name:
            update_data['full_name'] = full_name
        if bio:
            update_data['bio'] = bio
        if profile_picture_url:
            update_data['profile_picture_url'] = profile_picture_url

        if not update_data:
            return jsonify({"message": "No fields to update"}), 400

        # Update the user in the database
        result = users_collection.update_one({"_id": user_id}, {"$set": update_data})

        if result.modified_count > 0:
            return jsonify({"message": "Profile updated successfully!"}), 200
        else:
            return jsonify({"message": "User not found or no changes applied"}), 404

    except Exception as e:
        print(f"Error updating profile: {e}")
        return jsonify({"message": "Failed to update profile. Please try again later."}, 500)
    
if __name__ == "__main__":
    app.run(debug=True, port=5001) 
