
# HTTP REQUESTS METHOD
# GET: FOR ONLY DATA RETREIVAL
# POST: SUBMITS AN ENTITY TO THE SPECIFIED RESOURCE
# PUT: IS USED TO REPLACE ALL CURRENT REPRESENTATION OF TARGET RESOURCE
# DELETE: DELETES THE SPECIFED RESOURCE


# store a list of user to our database and expose the API
# so that we can delete, update and get user and so on

from typing import Optional, List
from models import User, Role, Gender, UserUpdateRequest  # Ensure these are defined correctly in the models file
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# Sample database initialized as a list of User instances

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
    ),

    User(
    id = UUID ('d150e319-8030-4910-ac6e-678b5f980b78'),
    first_name = "Rahul",
    last_name = "Puri",
    gender = Gender.male,
    roles = [
      Role.admin
    ]
    ),

    User(
    id = uuid4(),
    first_name = "Wahaj",
    last_name = "Rasheed",
    gender = Gender.male,
    roles = [
      Role.admin
    ]
    )
]

# BASIC GET
@app.get('/')
def root():
    return {'Hello': 'Hubex'}

# GET METHOD
@app.get('/api/v1/users')
async def fetch_users():
    return db;

# POST METHOD
@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {'id':user.id}

# DELETE METHOD
@app.delete("/api/v1/users/{user_id}")
async def delete(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            # if user_update.middle_name is not None:
            #     user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
            status_code = 404,
            detail=f"user with id: {user_id} does not exists" 
        )
