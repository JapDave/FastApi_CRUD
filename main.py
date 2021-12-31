from fastapi import FastAPI,File,UploadFile

from routes.user import user
app = FastAPI()
app.include_router(user)



# @app.post("/students")
# async def create_student(user:Student):
#    user = db.Students.insert_one(user.dict(by_alias=True))
#    return {'user': user}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}
