from tkinter import CASCADE
from . database import Base
from sqlalchemy.sql.expression import null, text
from sqlalchemy import TIMESTAMP,String, Integer,Boolean,Column,ForeignKey
from sqlalchemy.orm import relationship

class Table1(Base): #columns for the sproduct sellers for posting
    __tablename__ = "sellers"

    id=Column(Integer, nullable=False,primary_key=True)
    item_photo=Column(String, nullable=True)
    item_video=Column(String, nullable=True)
    item_name=Column(String, nullable=True)
    item_discription = Column(String, nullable=True)
    item_price= Column(String,nullable=True)
    item_qty= Column(String,nullable=True)
    item_availability =Column(Boolean,server_default=text("True"), nullable=False)
    item_makers=Column(String, nullable=True)
    item_distributor= Column(String, nullable=True)
    created_at =Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))
    owner_id=Column(Integer,ForeignKey("ksellers.id",ondelete="CASCADE"),nullable=False)

    # in other to create the show the info of whocreates a post, we would have to establish a reltionship and to donthat , we would write the following codes
    owner =relationship("TableUser1")



class Table2(Base): #columns for the service renderers
    __tablename__ = "services"

    id=Column(Integer, nullable=False,primary_key=True)
    sample_photo=Column(String, nullable=True)
    sample_video=Column(String, nullable=True)
    sample_name=Column(String, nullable=True)
    sample_discription = Column(String, nullable=True)
    sample_pricing= Column(String,nullable=True)
    availability=Column(String, nullable=True)   
    created_at =Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))


class TableUser1(Base):
    __tablename__ = "ksellers"

    id=Column(Integer,primary_key=True, nullable=False)
    biz_logo=Column(String, nullable=True)
    Owners_fullname=Column(String, nullable=True)
    biz_name=Column(String, nullable=True)
    biz_location=Column(String, nullable=True)
    biz_bio=Column(String, nullable=True)
    biz_type=Column(String, nullable=True)
    kshop_id= Column(String, nullable=True)
    biz_email= Column(String, nullable=False,unique=True)
    biz_contact1=Column(String, nullable=True)
    biz_contact2= Column(String, nullable=True)
    biz_market=Column(String, nullable=True)
    biz_line= Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    origin=Column(String, nullable=True)
    bvn=Column(String, nullable=True)
    gender=Column(String, nullable=False)
    dob=Column(String, nullable=True)
    card_details= Column(String, nullable=True)
    bank_name=Column(String, nullable=True)
    bank_number= Column(Integer, nullable=True)
    branch_location=Column(String, nullable=True)
    lga=Column(String, nullable=True)
    nationality=Column(String, nullable=True)
    passcode=Column(String, nullable=False)
    password=Column(String, nullable=False)


class TableUser2(Base):
    __tablename__ ="kservicerenderers"

    id=Column(Integer,primary_key=True,nullable=None)
    biz_name=Column(String, nullable=False)
    biz_location=Column(String, nullable=False)
    biz_bio=Column(String, nullable=False)
    biz_type=Column(String, nullable=False)
    kshop_id=Column(String, nullable=False)
    biz_email=Column(String, nullable=False,unique=True)
    biz_contact1=Column(Integer, nullable=False)
    biz_contact2=Column(Integer, nullable=False)
    biz_market=Column(String, nullable=False)
    biz_category=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("NOW()"))
    origin=Column(String, nullable=False)
    bvn=Column(Integer, nullable=False)
    gender=Column(String, nullable=False)
    dob=Column(String, nullable=False)
    card_details=Column(Integer, nullable=False)
    bank_name=Column(String, nullable=False)
    bank_number=Column(Integer, nullable=False)
    branch_location=Column(String, nullable=False)
    lga=Column(String, nullable=False)
    nationality=Column(String, nullable=False)
    passcode=Column(Integer, nullable=False)
    password=Column(String,nullable=True)


class TableUser3(Base):
    __tablename__="buyers"

    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String, nullable=False,unique=True)
    password=Column(String, nullable=False)
    dp=Column(String, nullable=True)
    gender=Column(String,nullable=False)
    contact_number=Column(String,nullable=True)
    card_details=Column(String, nullable=True)
    comment=Column(String, nullable=True)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text("Now()"), nullable=False ) 
    Ratings=Column(Integer, nullable=True)
    name=Column(String,nullable=False)
    
class Votes(Base):
    __tablename__="votes"

    post_id=Column(Integer,ForeignKey("sellers.id", ondelete=CASCADE), primary_key=True)
    user_id=Column(Integer,ForeignKey("ksellers.id",ondelete=CASCADE),primary_key=True)


 