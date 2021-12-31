from fastapi import APIRouter
from fastapi import UploadFile,File,Form
from pydantic.networks import EmailStr
from models.user import User
from config.db import conn
from schemas.user import userEntity,users

user = APIRouter()

@user.get('/users')
async def get_users():
   return users(conn.Fastapi.user.find())



@user.post('/adduser', response_model=User)
async def create_user(name:str = Form(...),
                     email:EmailStr=Form(...),
                     password:str=Form(...),
                     age:int=Form(...),
                     profile:UploadFile=File(...)):
   try:
      
      adduser = User(name=name,email=email,password=password,age=age,profile=profile.filename)
      res = conn.Fastapi.user.insert_one(dict(adduser))
      return conn.Fastapi.user.find_one({'_id':res.inserted_id})
   
   except Exception as e:
      return e
    