from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
import asyncio
from models import User, Gender, Role, UserUpdate

# db is a list of users

db: List[User] = [
    User(id=UUID('99b218a1-8d94-48a6-9bcd-eb027ad919c2'),
         fName='Sam',
         lName='Roy',
         gender=Gender.male,
         role=[Role.student]),
    User(id=UUID('71c68169-d638-4c0f-8865-e33135c97574'),
         fName='Rima',
         lName='Dey',
         gender=Gender.female,
         role=[Role.user]),
    User(id=UUID('5c8cfee8-f364-4509-945c-a8d442197768'),
         fName='Prat',
         lName='Bose',
         gender=Gender.male,
         role=[Role.admin, Role.user])
]

app = FastAPI()


@app.get('/{id}')  # get request to the root , get http method
async def root(id: int):
    return {'name': 'Sourima', 'id': id}


@app.get('/api/v1/user')
async def get_user():
    return db


@app.get('/api/v1/id/gender')
async def get_id_gender():
    id_list = [{'id': i.id, 'gender': i.gender.value} for i in db]
    return id_list


@app.post('/api/v1/user')
async def register(user: User):
    db.append(user)
    return {'id': user.id}


@app.delete('/api/v1/user/{u_id}')
async def remove_user(u_id):
    for user in db:
        if user.id == u_id:
            db.remove(user)
            return db

    raise HTTPException(
        status_code=200,
        detail=f'The user id {u_id} does not exist'
    )


@app.put('/api/v1/user/{user_id}')
async def update_user(user_update: UserUpdate, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.fName is not None:
                user.fName = user_update.fName
            if user_update.lName is not None:
                user.lName = user_update.lName
            if user_update.mName is not None:
                user.mName = user_update.mName
            if user_update.role is not None:
                user.role = user_update.role
            return
    raise HTTPException(
        status_code=404,
        detail=f'The user id {user_id} does not exist'
    )
