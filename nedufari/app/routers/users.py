
from fastapi import Depends,APIRouter,Response,status,HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, utils
from typing import List

router= APIRouter(tags=["users"])


############################################ cruds for the seller user ###################################################
# for the fact that we bump into probl,s i hve decided to dosnlod
@router.post("/user_seller",status_code=status.HTTP_202_ACCEPTED,)
def seller_user(instance:schemas.SellerUser, db:Session=Depends(database.get_db)):
    hashed1=utils.hash_password(instance.password)
    instance.password=hashed1
    data= models.TableUser1(**instance.dict())
    print
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@router.delete("/user_seller/{id}")
def delete_user(id:int, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser1).filter(models.Table1.id==id)
    if data.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id is not found ")
    db.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/user_seller/{id}")
def update_user(id:int, instance:schemas.SellerUser, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser1).filter(models.TableUser1.id==id)
    index=data.first()

    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id {id} is not found ")
    db.update(instance.dict(),synchronize_session=False)
    db.commit()
    return index
    



#######################################cruds for the seller user ##############################################################

@router.post("/user_service", status_code=status.HTTP_202_ACCEPTED,response_model=schemas.serviceuserResponse)
def service_user(instance:schemas.ServiceUser, db:Session=Depends(database.get_db)):

    hashed1= utils.hash_password(instance.password)
    instance.password=hashed1
    
    data= models.TableUser2(**instance.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data


@router.delete("/user_service/{id}")
def delete_user(id:int, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser2).filter(models.TableUser2.id==id)
    if data.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id is not found ")
    db.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/user_seller/{id}")
def update_user(id:int, instance:schemas.ServiceUser, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser2).filter(models.TableUser2.id==id)
    index=data.first()

    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id is not found ")
    db.update(instance.dict(),synchronize_session=False)
    db.commit()
    return index



##########################################  cruds for the buyer user ####################################################


@router.post("/user_buyer", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ResponseBuyer)
def buyer_user(instance:schemas.BuyerUser, db:Session=Depends(database.get_db)):
    hashed1=utils.hash_password(instance.password)
    instance.password=hashed1
    new_data=models.TableUser3(**instance.dict())
    print(new_data)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@router.delete("/user_buyer/{id}")
def delete_user(id:int, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser3).filter(models.TableUser3.id==id)
    if data.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id is not found ")
    db.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/user_buyer/{id}")
def update_user(id:int, instance:schemas.BuyerUser, db:Session=Depends(database.get_db)):
    data= db.query(models.TableUser3).filter(models.TableUser3.id==id)
    index=data.first()

    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the data with the id is not found ")
    db.update(instance.dict(),synchronize_session=False)
    db.commit()
    return index