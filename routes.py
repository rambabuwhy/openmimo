from fastapi import FastAPI
import logpkg as LOG

app = FastAPI()

# Sample user data
users = {
    1: {"username": "user1", "email": "user1@example.com"},
    2: {"username": "user2", "email": "user2@example.com"},
}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    #LOG.INFO('This is an info message')
    if user_id in users:
        return users[user_id]
    else:
        return {"error": "User not found"}

# To run the FastAPI application
# Use the following command in your terminal:
# uvicorn filename:app --reload
# Replace "filename" with the actual name of your Python file.
