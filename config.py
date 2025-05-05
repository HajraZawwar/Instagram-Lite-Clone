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
    aws_access_key_id=os.getenv('AKIAZURXUCXMN2EDQ55Q'),
    aws_secret_access_key=os.getenv('sYb8Za0cxYoVxWbC3LF/sB8JOSdqVy/Bi77pznfE'),
    region_name=os.getenv('Europe (Stockholm) eu-north-1')
)
bucket_name = os.getenv('myawsbucket8777')

MONGO_URI = os.getenv("mongodb+srv://hajrazawwarmalik:<db_password>@instagramlitecluster.tlxvfb7.mongodb.net/?retryWrites=true&w=majority&appName=InstagramLiteCluster")
S3_BUCKET_NAME = os.getenv("myawsbucket8777")
AWS_ACCESS_KEY_ID = os.getenv("AKIAZURXUCXMN2EDQ55Q")
AWS_SECRET_ACCESS_KEY = os.getenv("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")
REGION_NAME = os.getenv("REGION_NAME", "Europe (Stockholm) eu-north-1")
USE_DYNAMODB = os.getenv("USE_DYNAMODB", "False") == "True"
