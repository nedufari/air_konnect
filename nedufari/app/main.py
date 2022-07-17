from fastapi import FastAPI
from . import database,models
from .database import Sessionlocal, engine
from .routers import products, service,users,auth,votes
#from .config import BaseSettings
from fastapi.middleware.cors import  CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins=["*"]#list of domains that can talk to our api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #you can specify the specifc domains you wish to talk to your api
    allow_credentials=True,
    allow_methods=["*"],#you can also specify the kind of methods you want them to do with the api, you may decide to either allow them do a get request, a put request, a delete request. you simply can tell them what you can only give them access to
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
