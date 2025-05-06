# 📸 Instagram Lite Clone

A lightweight Instagram clone built with Flask, MongoDB, and AWS S3. This application allows users to register, log in, upload images, and view a feed of posts.

---

## 🚀 Features

* User Registration and Authentication
* Image Uploads to AWS S3
* Post Feed Display
* Secure Credential Management with Environment Variables
* RESTful API Endpoints([flask-s3.readthedocs.io][1])

---

## 🧰 Tech Stack

* **Backend:** Flask, Flask-PyMongo
* **Database:** MongoDB Atlas
* **Cloud Storage:** AWS S3
* **Environment Management:** python-dotenv
* **Testing:** pytest([MongoDB][2], [Medium][3])

---

## 📁 Project Structure

```

instagram-lite-clone/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── templates/
│   └── ...
├── static/
│   └── ...
├── routes/
│   └── ...
├── models/
│   └── ...
└── tests/
    └── test_config.py
```



---

## ⚙️ Setup Instructions

###

```bash
git clone https://github.com/HajraZawwar/Instagram-Lite-Clone.git
cd Instagram-Lite-Clone
```

([YouTube][4])

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```



### 3. Install Dependencies

```bash
pip install -r requirements.txt
```



### 4. Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```ini
# MongoDB
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/insta_db?retryWrites=true&w=majority

# AWS
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=eu-north-1
S3_BUCKET_NAME=myawsbucket8777

# Flask
SECRET_KEY=your-flask-secret-key
USE_DYNAMODB=False
```



**Note:** Ensure that `.env` is added to `.gitignore` to prevent sensitive information from being committed.

### 5. Run the Application

```bash
python app.py
```



The application will be accessible at `http://localhost:5000/`.

---

## 🧪 Running Tests

To run the test suite:

```bash
pytest
```



This will execute all tests located in the `tests/` directory.

---

## 📦 Deployment

For deploying the application:

* **AWS EC2:** Host the Flask application.
* **MongoDB Atlas:** Use as the cloud database service.
* **AWS S3:** Store and serve uploaded images.

Ensure that all environment variables are properly set in your production environment.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

For more details on integrating Flask with MongoDB and AWS S3, you can refer to this [project guide](https://medium.com/@jdiasdacostalima/project-idea-creating-a-flask-app-with-mongodb-aws-and-git-f59973631a56).([Medium][3])

---

[1]: https://flask-s3.readthedocs.io/?utm_source=chatgpt.com "Flask-S3 — flask-S3 0.3.2 documentation"
[2]: https://www.mongodb.com/resources/products/compatibilities/setting-up-flask-with-mongodb?utm_source=chatgpt.com "Flask-PyMongo With MongoDB Atlas Guide"
[3]: https://medium.com/%40jdiasdacostalima/project-idea-creating-a-flask-app-with-mongodb-aws-and-git-f59973631a56?utm_source=chatgpt.com "Project Idea: Creating a Flask App with MongoDB, AWS, and Git"
[4]: https://www.youtube.com/watch?v=tJxMPvzkCyo&utm_source=chatgpt.com "Flask and MongoDB w/ Flask-pymongo | Project Setup - YouTube"

---

# 🚀 Let's Connect the World with SnapConnect!


