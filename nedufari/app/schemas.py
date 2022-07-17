
from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime, timedelta, timezone, time



class SellerUser(BaseModel):
    biz_logo:str
    Owners_fullname:str
    biz_name:str
    biz_location:str
    biz_bio:str
    biz_type:str
    #kshop_id: str
    biz_email: EmailStr
    biz_contact1:str
    biz_contact2: str
    biz_market:str
    biz_line: str
    #created_at:datetime
    origin:str
    bvn:str
    gender:str
    #dob:datetime
    #card_details: str
    #bank_name:str
    #bank_number: str
    branch_location:str
    lga:str
    nationality:str
    password:str
    passcode:str

class ResponseSellerUser( SellerUser):
    created_at:datetime
    id:int
    class Config:
        orm_mode=True




class SellersPost(BaseModel):
    item_photo:str
    item_video:str
    item_name: str
    item_discription : str
    item_price: str
    item_qty: str
    item_availability: bool = True
    item_makers:str
    item_distributor: str

class postcreated(SellersPost):
    id: int
    created_at:datetime
    owner_id: int
    class config:
        orm_mode=True

   

class SellersPostResponse(SellersPost):
    id: int
    created_at:datetime
    owner_id: int
    owner: ResponseSellerUser
    

    class Config:
        orm_mode=True

class PostOut(SellersPost):
    Table1:SellersPostResponse
    total_votes:int
    
    class Config:
        orm_mode=True



class servicePost(BaseModel):
    sample_photo:str
    sample_video:str
    sample_name: str
    sample_discription: str
    sample_pricing: str
    id: int
    created_at:datetime



##################################################################################################################


class ServiceUser(BaseModel):
    biz_name:str
    biz_location:str
    biz_bio:str
    biz_type:str
    kshop_id: str
    biz_email: EmailStr
    biz_contact1:int
    biz_contact2: int
    biz_market:str
    biz_category: str
    created_at:datetime
    origin:str
    bvn:str
    gender:str
    dob:datetime
    card_details: str
    bank_name:str
    bank_number: str
    branch_location:str
    lga:str
    nationality:str
    password:str
    passcode:int

class serviceuserResponse(BaseModel):
    ceated_at:datetime
    id:int
    class Config:
        orm_mode=True



class BuyerUser(BaseModel):
    #id:int
    name:str
    email:EmailStr
    password:str
    dp:str
    gender:str
    #comments:str
    #ratings :int 
    contact_number:str
    #created_at:datetime


class ResponseBuyer(BaseModel):
    created_at : datetime
    info:str="welcome to konnect "
    password:str
    
    class Config:
        orm_mode=True


class Login(BaseModel):
    email:EmailStr
    password:str 




# schema for the token authentication, the acess tokena nd the token type
class AccessToken(BaseModel):
    access_token:str
    token_type:str
    class Config:
        orm_mode=True

        

class TokenData(BaseModel):
    id: str=Optional[int]



class vote(BaseModel):
    post_id: int
    direction: conint(le=1)