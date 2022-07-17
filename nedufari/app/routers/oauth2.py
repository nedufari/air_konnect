from fastapi import Depends, HTTPException,Response,status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from .. import schemas,database,models
from datetime import datetime,timedelta
from sqlalchemy.orm import Session
from ..config import settings


#we need three parameters, the algorithm, the expiration and the secretkey

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

SECRETE_KEY=  settings.secret_key#"mjaXjissiosjbcjnoixhbljsmjabbinjnsjo" # this jibrish would be changed 
ALGORITHM= settings.algorithm#"HS256" # this is the default algorithm for thr jwt
EXPIRED= settings.expired#10 #this is a changable time although set in minutes 

def create_token(data:dict): # this function is passed with the a dictionary instanvce
    to_encode= data.copy()  #this ois the line that makes the token

    expire=datetime.utcnow() + timedelta (minutes=EXPIRED) # this line makes the token expire and another is generated
    to_encode.update({"exp":expire}) #update the expiration date 

    encoded_jwt= jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHM)

    return encoded_jwt #this would produce the token 

def verify_token(token:str, data_exception):
    try:
        payload=jwt.decode(token,SECRETE_KEY,[ALGORITHM]) #this would recieve the tokan and vrify it
        id : str = payload.get("user_id") 
        if id == None:
            raise data_exception
        token_data=schemas.TokenData(id=id)
    except JWTError:
        raise data_exception
    return token_data

def get_parentUser(token:str=Depends(oauth2_scheme),db: Session=Depends(database.get_db)):
    credential_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
    detail=f"could not validate credentials ",headers={"WWW-Authenticate" : "bearer"})
    token= verify_token(token,credential_exception)

    user=db.query(models.TableUser1).filter(models.TableUser1.id==token.id).first()
    return user 

        

