from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    
    User(
         id = uuid4(), 
         first_name = 'Jamila',
         last_name = 'Ahmed',
         gender = Gender.female,
         roles = [Role.student]
    ),

    User(
         id = uuid4(), 
         first_name = 'Alex',
         last_name = 'Jones',
         gender = Gender.male,
         roles = [Role.admin, Role.user]
    )   

]

# making get request for retreiving the data
# There are four methods, GET, POST,  PUT, DELETE

# endpoint
@app.get('/')
async def root ():
    return {'Hello' : 'Asad'}

# endpoint
@app.get('/api/v1/users')
async def fetch_users():
    return db;