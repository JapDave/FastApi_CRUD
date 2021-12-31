
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic import Field



class User(BaseModel):
   name: str
   email: EmailStr
   password: str
   age: int = Field(...,gt=0)
   profile: str
