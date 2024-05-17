# #  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# # .\.venv\Scripts\activate # IF NAME OF THE VENV IS .VENV

# # There are four HTTP methods
# # GET, PUT, POST, DELETE


# # HTTP REQUESTS METHOD

# # GET: FOR ONLY DATA RETREIVAL

# # POST: SUBMITS AN ENTITY TO THE SPECIFIED RESOURCE

# # PUT: IS USED TO REPLACE ALL CURRENT REPRESENTATION OF TARGET RESOURCE

# # DELETE: DELETES THE SPECIFED RESOURCE


# # store a list of user to our database and expose the API
# # so that we can delete, update and get user and so on

from typing import Optional, List
from models import User, Role, Gender  # Ensure these are defined correctly in the models file
from fastapi import FastAPI
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# # Sample database initialized as a list of User instances

db: List[User] = [
    User(
        id = UUID ('e1652b25-b727-4168-ab7e-5fd0814fae53'), # passing I.D in string to keep it fixed
        first_name='Jamila',
        last_name='Ahmed',
        gender=Gender.female,
        roles=[Role.student]
    ),

    User(
        id = uuid4(),
        first_name='Alex',
        last_name='jones',
        gender=Gender.male,
        roles=[Role.user]
    )
]

@app.get('/')
def root():
    return {'Hello': 'Hubex'}

@app.get('/api/v1/users')
async def fetch_users():
    return db;

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {'id':user.id}
