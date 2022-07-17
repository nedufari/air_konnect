from multiprocessing import synchronize
from fastapi import APIRouter,Response,status,Depends,HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models
from . import auth, oauth2

router=APIRouter(tags=["products post"])

@router.post("/products")
def post_product(instnce:schemas.SellersPost, db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_parentUser)):
    data= models.Table1(**instnce.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    
    return data

@router.get("/products")
def get_all(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_parentUser)):
    data= db.query(models.Table2).all()
    return data

@router.get("/products/{id}")
def get_one(id:int, db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_parentUser)):
    data= db.query(models.Table2).filter(models.Table2.id==id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the record with id {id} not found")
    return data

@router.delete("/products/{id}")
def delete_product(id:int, db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_parentUser)):
    data=db.query(models.Table2).filter(models.Table2.id==id)

    if data.first() ==None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"record with id {id} not found")
    db.delete(synchronize_session=False)
    db.commit()
    return Response (status_code=status.HTTP_204_NO_CONTENT)

def update_product(id:int, instance:schemas.servicePost,db:Session=Depends(get_db), user_id:int=Depends(oauth2.get_parentUser)):

    data= db.query(models.Table2).filter(models.Table2.id==id)
    index=data.first()

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"record with id {id} not found")
    data.update(instance.dict(), synchronize_session=False)
    db.commit()
    return index

        
