from pydantic import BaseModel, EmailStr, validator, root_validator
import string
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    age: int
    email: Optional[EmailStr]
    phone_number: Optional[str]
    
    @root_validator(pre=True)
    def validate_email_phone(cls, values):
        if "email" in values or "phone_number" in values:
            return values
        else:
            raise ValueError("Must provide an email or phone number")
    
    @validator("username")
    def validate_username(cls, value):
        if any(char in string.punctuation for char in value):
            raise ValueError("Unexpected punctuation symbol in username")
        else:
            return value
        
    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if any(d in string.digits for d in value): 
            return value
        else:
            raise ValueError("Password must contain at least one number")
    
    
user = User(username="jimmy", password="demo1234", age=21, email="jimmy@ucdavis.edu")
print(user)
