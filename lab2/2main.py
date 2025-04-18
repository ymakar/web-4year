from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
import operator

app = FastAPI()


class Comment(BaseModel):
    id: str
    content: str

class Post(BaseModel):
    id: str
    title: str
    content: str
    comments: List[Comment] = []

class User(BaseModel):
    id: str
    name: str
    email: str
    posts: List[Post] = []



users: List[User] = []



def find_user(user_id: str) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

def find_post(user: User, post_id: str) -> Post:
    for post in user.posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")




@app.post("/users", response_model=User)
def create_user(name: str, email: str):
    user = User(id=str(uuid4()), name=name, email=email)
    users.append(user)
    return user

@app.get("/users", response_model=List[User])
def list_users(skip: int = 0, limit: int = 10, sort_by: str = "name", reverse: bool = False):
    try:
        sorted_users = sorted(users, key=operator.attrgetter(sort_by), reverse=reverse)
        return sorted_users[skip: skip + limit]
    except AttributeError:
        raise HTTPException(status_code=400, detail="Invalid sort field")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, name: Optional[str] = None, email: Optional[str] = None):
    user = find_user(user_id)
    if name:
        user.name = name
    if email:
        user.email = email
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    global users
    users = [u for u in users if u.id != user_id]
    return {"detail": "User deleted"}



@app.post("/users/{user_id}/posts", response_model=Post)
def create_post(user_id: str, title: str, content: str):
    user = find_user(user_id)
    post = Post(id=str(uuid4()), title=title, content=content)
    user.posts.append(post)
    return post

@app.get("/users/{user_id}/posts", response_model=List[Post])
def list_posts(user_id: str):
    user = find_user(user_id)
    return user.posts



@app.post("/users/{user_id}/posts/{post_id}/comments", response_model=Comment)
def create_comment(user_id: str, post_id: str, content: str):
    user = find_user(user_id)
    post = find_post(user, post_id)
    comment = Comment(id=str(uuid4()), content=content)
    post.comments.append(comment)
    return comment

@app.get("/users/{user_id}/posts/{post_id}/comments", response_model=List[Comment])
def list_comments(user_id: str, post_id: str):
    user = find_user(user_id)
    post = find_post(user, post_id)
    return post.comments


'''
uvicorn 2main:app --reload  #Запуск сервера
POST /users?name=John&email=john@example.com   #Створити користувача
GET /users?skip=0&limit=5&sort_by=email&reverse=true   #Отримати список користувачів (із пагінацією та сортуванням)
POST /users/{user_id}/posts?title=MyPost&content=HelloWorld  #Додати пост
POST /users/{user_id}/posts/{post_id}/comments?content=NicePost   #Додати коментар

'''