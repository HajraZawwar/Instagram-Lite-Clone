# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_router
from routes.post_routes import router as post_router

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(user_router, prefix="/api/users")
app.include_router(post_router, prefix="/api/posts")

@app.get("/")
def read_root():
    return {"message": "SnapConnect API is running."}
