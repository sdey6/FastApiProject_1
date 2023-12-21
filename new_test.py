from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/about')
async def get_about():
    return {f"This page is a short description for FastApi"}
