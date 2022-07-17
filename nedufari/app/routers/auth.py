from fastapi import APIRouter,Response,status,Depends,HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models,utils
from . import oauth2
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(tags=["authentication"])

@router.post("/login1",response_model=schemas.AccessToken) #sellers
def Login1(instance:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    owner= db.query(models.TableUser1).filter(models.TableUser1.biz_email==instance.username).first()

    if not owner :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    if utils.verify_passowrd(instance.password, owner.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")

    access_token= oauth2.create_token(data={"user_id":owner.id})   
    return {"access_token":access_token, "token_type":"bearer"}



@router.post("/login2",response_model=schemas.AccessToken)#service
def Login2(instance:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    owner= db.query(models.TableUser2).filter(models.TableUser2.biz_email==instance.username).first()

    if not owner:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    if utils.verify_passowrd(instance.password, owner.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    access_token= oauth2.create_token(data={"user_id":owner.id})
    return {"access_token":access_token, "access_type":"bearer"}


@router.post("/fari",response_model=schemas.AccessToken) 
def Login3(instance:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    owner= db.query(models.TableUser3).filter(models.TableUser3.email==instance.password).first()
    
    

    if not owner :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    if utils.verify_passowrd(instance.password, owner.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    access_token=oauth2.create_token(data={"user_id":owner.id})
    return {"access_token":access_token, "access_type":"bearer"}


 #"$2b$12$03.YoohrHav.AqvSsZsiYe/P25EnVZly9xXerscDFe2TKLQtMvIRm"