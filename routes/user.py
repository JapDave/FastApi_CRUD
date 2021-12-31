from bson.objectid import ObjectId
from fastapi import APIRouter
from fastapi import UploadFile,File,Form
from pathlib import  Path

from pydantic.networks import EmailStr
from models.user import User
from config.db import conn
from schemas.user import userEntity,users
import shutil
import os

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
      upload_folder = open(os.path.join('./uploads', profile.filename), 'wb+')
      shutil.copyfileobj(profile.file, upload_folder)
      upload_folder.close()
      adduser = User(name=name,email=email,password=password,age=age,profile=profile.filename)
      res = conn.Fastapi.user.insert_one(dict(adduser))
      print(res.inserted_id)
      return conn.Fastapi.user.find_one({'_id':res.inserted_id})
   
   except Exception as e:
      return e

@user.get('/user/{id}')
async def get_user(id):
   try:
      return userEntity(conn.Fastapi.user.find_one({'_id':ObjectId(id)}))
   except Exception as e:
      pass

@user.put('/updateuser/{id}',response_model=User)
async def update_user(id,name:str = Form(...),
                     email:EmailStr=Form(...),
                     password:str=Form(...),
                     age:int=Form(...),
                     profile:UploadFile=File(...)):
      try:
         user_obj = User(name=name,email=email,password=password,age=age,profile=profile.filename)
         
         conn.Fastapi.user.find_one_and_update({'_id':ObjectId(id)},{
            '$set':dict(user_obj)
         })
            
         return userEntity(conn.Fastapi.user.find_one({'_id':ObjectId(id)}))
      except Exception as e:
         pass

@user.delete('/deleteuser/{id}')
async def delete_user(id):
   try:
      conn.Fastapi.user.find_one_and_delete({'_id':ObjectId(id)})
      return 'User Deleted'
   except Exception as e:
      print(e)