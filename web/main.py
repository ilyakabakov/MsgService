from fastapi import FastAPI, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List
from bson import ObjectId
from fastapi_pagination import Page, paginate, add_pagination

app = FastAPI()

client = AsyncIOMotorClient("mongodb://mongo:27017")
db = client["messages_db"]
collection = db["messages"]


class Message(BaseModel):
    id: str
    text: str
    author: str


class CreateMessage(BaseModel):
    text: str
    author: str


@app.get("/api/v1/messages/", response_model=Page[Message])
async def get_messages():
    messages = await collection.find().to_list(1000)
    return paginate([Message(id=str(msg["_id"]), text=msg["text"], author=msg["author"]) for msg in messages])


@app.post("/api/v1/message/")
async def create_message(message: CreateMessage):
    result = await collection.insert_one(message.dict())
    return {"id": str(result.inserted_id)}


add_pagination(app)
