from flask import Flask, request, jsonify,url_for
from flask_cors import CORS
from pymongo import MongoClient
import uuid
from datetime import datetime
from flask_bcrypt import Bcrypt
import os
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
import boto3
from pymongo import MongoClient

load_dotenv()

# MongoDB
mongo_uri = os.getenv('MONGO_URI')
mongo_client = MongoClient(mongo_uri)
db = mongo_client['insta_db']  # Or your actual db name

# AWS S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('S3_REGION')
)
bucket_name = os.getenv('S3_BUCKET_NAME')


app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)  # Initialize Flask-Bcrypt

# MongoDB connection
client = MongoClient('mongodb+srv://hajrazawwarmalik:7KnkNxNRfuHxttSa@instagramlitecluster.tlxvfb7.mongodb.net/?retryWrites=true&w=majority&appName=InstagramLiteCluster')
db = client['instagram_lite']
users_collection = db['users']
posts_collection = db['posts']

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads'  # Folder where images will be saved
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image file extensions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Set the folder for Flask to use

# Ensure the upload folder exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400  # If no file is sent
    
    file = request.files['image']  # Get the file from the request
    caption = request.form.get('caption')  # Get the caption text from the form
    user_id = request.form.get('user_id')  # Get the user ID from the form

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400  # If the file is empty
    
    if file and allowed_file(file.filename):  # Check if the file has an allowed extension
        # Secure the filename to avoid malicious files
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Path to save the file
        
        file.save(filepath)  # Save the file to the folder

        # Save the post details to the database
        post = {
            "_id": str(uuid.uuid4()),  # Generate a unique post ID
            "user_id": user_id,
            "caption": caption,
            "media_url": filepath,  # Save the file path to the database
            "created_at": datetime.utcnow(),
            "likes": 0,
            "comments": []  # Start with no comments
        }
        posts_collection.insert_one(post)  # Insert the post into MongoDB

        return jsonify({"message": "Post uploaded successfully!"}), 201  # Success response
    else:
        return jsonify({"message": "Invalid file type"}), 400  # If the file type is not allowed


# Get Feed API
@app.route('/feed', methods=['GET'])
def feed():
    posts = list(posts_collection.find({}).sort("created_at", -1))  # Get posts sorted by time
    for post in posts:
        post['_id'] = str(post['_id'])  # Convert MongoDB ObjectId to string
        # Correct the media_url so it can be used in the frontend
        post['media_url'] = url_for('static', filename='uploads/' + post['media_url'].split('/')[-1])
    return jsonify(posts), 200  # Return posts in the feed
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
    
# Add Comment API
@app.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    post_id = data.get('post_id')
    user_id = data.get('user_id')
    text = data.get('text')

    if not post_id or not user_id or not text:
        return jsonify({"message": "Missing required fields"}), 400

    try:
        comment = {
            "user_id": user_id,
            "text": text,
            "timestamp": datetime.utcnow()
        }
        result = posts_collection.update_one(
            {"_id": post_id},
            {"$push": {"comments": comment}}
        )

        if result.modified_count > 0:
            return jsonify({"message": "Comment added successfully!"}), 201
        else:
            return jsonify({"message": "Post not found"}), 404
    except Exception as e:
        print(f"Error adding comment: {e}")
        return jsonify({"message": "Failed to add comment. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
