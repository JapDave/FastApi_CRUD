def userEntity(item) -> dict():
   try:
    
      return {
         "id": str(item["_id"]),
         "name": item["name"], 
         "email": item["email"], 
         "password": item["password"],
         "age": item["age"],
         "profile":str(item["profile"])
         
      }
      
   except Exception as e:
      print(e)


def users(entity) -> list():
   try:
      return [userEntity(item) for item in entity]
   except Exception as e:
      print(e)