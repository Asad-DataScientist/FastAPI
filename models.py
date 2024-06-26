from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = 'Male'
    female = 'Female'

class Role(str, Enum):
    student = 'Student'
    admin = 'admin'
    user = 'User'

# Creating the user model
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    # middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    first_name: Optional [str]
    last_name: Optional [str]
    # middle_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]