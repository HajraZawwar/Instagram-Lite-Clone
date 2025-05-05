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

MONGO_URI = os.getenv("mongodb+srv://hajrazawwarmalik:<db_password>@instagramlitecluster.tlxvfb7.mongodb.net/?retryWrites=true&w=majority&appName=InstagramLiteCluster")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = os.getenv("REGION_NAME", "us-east-1")
USE_DYNAMODB = os.getenv("USE_DYNAMODB", "False") == "True"
