from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4


class Gender(Enum):
    male = 'male'
    female = 'female'
    others = 'others'


class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    fName: str
    lName: str
    mName: Optional[str] = None
    gender: Gender
    role: List[Role]


class UserUpdate(BaseModel):
    fName: Optional[str] = None
    lName: Optional[str] = None
    mName: Optional[str] = None
    role: Optional[List[Role]] = None
