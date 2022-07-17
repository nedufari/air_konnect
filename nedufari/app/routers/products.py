from logging import raiseExceptions
from multiprocessing import synchronize
from operator import contains
from unittest import result
from fastapi import APIRouter,Response,status,Depends,HTTPException
from sqlalchemy import true, func
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models
from . import oauth2
from typing import List,Optional


router=APIRouter(tags=["products post"])

@router.post("/products", response_model=schemas.SellersPostResponse)
def post_product(instnce:schemas.SellersPost, db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_parentUser)):

    print (current_user.id)
    data= models.Table1(owner_id=current_user.id,**instnce.dict())
    db.add(data) 
    db.commit()
    db.refresh(data)
    
    return data

@router.get("/products", response_model=List[schemas.PostOut])
def get_all(db:Session=Depends(get_db), current_user:int=Depends(oauth2.get_parentUser),limits:int=10, skip:int=0,search:Optional[str]=""):
    #the skip parameter and the limits parameter are the parimeters that would serve the user the users need for queries
    #the skip is also how we are gping to do pagination on th front end
    #  data= db.query(models.Table1).filter(models.Table1.item_name.contains(search)).limit(limits).offset(skip).all()

     result=db.query(models.Table1, func.count(models.Votes.post_id).label("total_votes")).join(models.Votes,models.Votes.post_id==models.Table1.id,isouter=True).group_by(models.Table1.id).filter(models.Table1.item_name.contains(search)).limit(limits).offset(skip).all()
    #  this is a join command stored in reults, we would query the table and use the join function to select the tables and the specif columns 
    # you would love to joi, in this case, we wold love to join the product table with the vote table and th columns is the product.id and the vots.id to 
    # knw the amount of votes each procucts have.
    # we also grouped by the product.id and we are counting using the func.count method to get the number of votes 
    
     return result

@router.get("/products/{id}", response_model=List[schemas.PostOut])
def get_one(id:int, db:Session=Depends(get_db), currrent_user:int=Depends(oauth2.get_parentUser),limits:int=10,search:Optional[str]=""):
    # data= db.query(models.Table1).filter(models.Table1.id==id).first()
    data=db.query(models.Table1, func.count(models.Votes.post_id).label("total_votes")).join(models.Votes,models.Votes.post_id==models.Table1.id,isouter=True).group_by(models.Table1.id).filter(models.Table1.id==id).first()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the record with id {id} not found")
    return data

@router.delete("/products/{id}")
def delete_product(id:int, db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_parentUser)):
    data_query=db.query(models.Table1).filter(models.Table1.id==id)
    data=data_query.first()

    if data ==None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"record with id {id} not found")
    if data.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not authorized to perform requested action ")
    data_query.delete(synchronize_session=False)
    db.commit()
    return Response (status_code=status.HTTP_204_NO_CONTENT)

@router.put("/products/{id}")
def update_product(id:int, instance:schemas.SellersPost,db:Session=Depends(get_db), current_user:int=Depends(oauth2.get_parentUser)):
 
    data= db.query(models.Table1).filter(models.Table1.id==id)
    index=data.first()

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"record with id {id} not found")
    if index.owner_id!=current_user.id:
        raise HTTPException (status_code=status.HTTP_403_FORBIDDEN, detail=f"you are not authorized to perform requested action")
    data.update(instance.dict(), synchronize_session=False)
    db.commit()
    return index

        
