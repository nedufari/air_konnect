from multiprocessing import synchronize
from fastapi import Depends, FastAPI, Response,HTTPException, status,APIRouter 
from sqlalchemy.orm import Session
from ..database import get_db
from ..routers import oauth2,auth
from .. import schemas, models



router=APIRouter(tags=['votes '],prefix="/votes")



@router.post("/")
def Votes(instance:schemas.vote, db:Session=Depends(get_db), current_user:int=Depends (oauth2.get_parentUser)):

    post =db.query(models.Table1).filter(models.Table1.id==instance.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the post with id {instance.post_id} does not exist")

    voter=db.query(models.Votes).filter(models.Votes.post_id==instance.post_id, models.Votes.user_id==current_user.id)
    found_voter=voter.first()
    if (instance.direction==1):
        if found_voter:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user{current_user.id} Already has a vote, so can't vote twice {instance.post_id}")
        new_voter=models.Votes(post_id=instance.post_id, user_id=current_user.id) #tthis is to register new vote if none is found
        db.add(new_voter)
        db.commit()
        return{"message":"Vote has been added successfully"}
    else:
        if not found_voter:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Votes does not exist")
            db.delete(synchronize_session=false)
            db.commit()
        return{"message":"votes has been deleted"}


    


    
#i think am gonna revisit this code and decie on making it two ways, so if the voter votes yes it has a different url and if the voter votes no, it also has a difgfeent url
# i think that solution makes more sense instead of compounding confusion, this is for the sake of those that wants to study the codes, but to me its all good though 