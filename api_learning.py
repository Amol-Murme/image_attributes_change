from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/bolg')
def create_blog(request:Blog):
    return {'data':f'blog is created as {request.title} and body is {request.body}'}



@app.get('/blogs')
def index(limit:int=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs'}
    else:
        return {'data':f'{limit} all blogs'}

@app.get('/about/{id}')
def about(id:int):
    return {'data':id}