# Instagram-Lite-Clone
# 📸 SnapConnect

A lightweight, minimal Instagram Lite Clone built with Flask, MongoDB, and basic HTML/CSS/JS.

---

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Design](#database-design)
- [UI/UX Screens](#uiux-screens)
- [Data Flow](#data-flow)
- [Setup Instructions](#setup-instructions)
- [Current Progress](#current-progress)
- [Next Steps](#next-steps)

---

## 📖 About the Project
SnapConnect is a mini social media platform that allows users to:
- Register and log in securely
- Upload posts with captions and images
- View a feed of latest posts
- Comment on posts
- Update their user profile

Built as part of an academic project to demonstrate a scalable backend system with a NoSQL database.

---

## ✨ Features
- 🔐 User Registration and Login
- 🖼️ Post Upload (Image + Caption)
- 📰 Feed Display (Newest First)
- 💬 Comment on Posts
- 🧑‍💼 Profile Update (Username, Bio, Profile Picture)

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Database:** MongoDB (Atlas Cloud DB)
- **Password Security:** Bcrypt (hashed storage)
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** RESTful APIs
- **Authentication:** Session-less, Token-based (future enhancement)

---

## 🗄️ Database Design

### Database: `instagram_lite`

| Collection | Fields |
|:-----------|:-------|
| **users** | `_id`, `email`, `password`, `username`, `full_name`, `bio`, `profile_picture_url` |
| **posts** | `_id`, `user_id`, `caption`, `media_url`, `created_at`, `likes`, `comments` |

### Example Document (users)
```json
{
  "_id": "bd72a256-c71c-4578-bd82-3b124a9856f0",
  "email": "user@example.com",
  "password": "$2b$12$....",
  "username": "cooluser",
  "full_name": "Cool User",
  "bio": "Love photography!",
  "profile_picture_url": "https://pics.com/image.jpg"
}
```

### Example Document (posts)
```json
{
  "_id": "fdd2a344-2b8e-4c19-8d0b-438b7a4e3fcd",
  "user_id": "bd72a256-c71c-4578-bd82-3b124a9856f0",
  "caption": "Beautiful sunset! 🌇",
  "media_url": "https://pics.com/sunset.jpg",
  "created_at": "2025-04-26T18:30:00Z",
  "likes": 0,
  "comments": []
}
```

---

## 🎨 UI/UX Screens

### Login Page
- **Fields:** Email, Password
- **Actions:** Login button, Sign-Up link

### Sign-Up Page
- **Fields:** Email, Username, Password, Confirm Password
- **Actions:** Sign-Up button, Login link

(Frontend screenshots will be uploaded soon!)

---

## 🔄 Data Flow

- **Registration:** New user registers ➔ `/register` API ➔ New user saved in `users` collection
- **Login:** Existing user logs in ➔ `/login` API ➔ Password verified
- **Uploading Post:** User submits caption and image ➔ `/upload` API ➔ Post saved in `posts` collection
- **Feed Loading:** Client calls `/feed` ➔ Backend fetches posts ➔ Posts displayed
- **Commenting:** User comments ➔ `/add_comment` API ➔ Comment pushed to the post document
- **Profile Update:** User updates info ➔ `/update_profile` ➔ User document updated

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/snapconnect.git
cd snapconnect
```

2. **Install required packages**
```bash
pip install flask flask-cors flask-bcrypt pymongo
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Access the application**
- Backend API will run at: `http://localhost:5001/`
- Frontend HTML files can be opened directly in the browser (or served with Flask if integrated).

---

## 🚀 Current Progress

| Module         | Status          |
|----------------|-----------------|
| User Registration | ✅ Completed |
| User Login        | ✅ Completed |
| Post Upload       | ✅ Completed |
| Feed Retrieval    | ✅ Completed |
| Comment System    | ✅ Completed |
| Profile Update    | ✅ Completed |
| Image Upload via File Browser | 🛠️ In Progress |

---

## 🛤️ Next Steps
- Improve image upload functionality (local upload and cloud storage)
- Add likes functionality
- Create post details page
- Improve frontend responsiveness
- Secure API endpoints
- Deployment (Render, Vercel, etc.)

---

## 📢 License
This project is for academic purposes. Feel free to use or contribute!

---

# 🚀 Let's Connect the World with SnapConnect!


