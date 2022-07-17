from fastapi import FastAPI
from . import database,models
from .database import Sessionlocal, engine
from .routers import products, service,users,auth,votes
#from .config import BaseSettings
from fastapi.middleware.cors import  CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins=["*"]#as of now
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
)


app.include_router(products.router)
app.include_router(service.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/post")
def get():
    return{"message":"hello world"}
