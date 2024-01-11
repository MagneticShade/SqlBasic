from db.database import Base

from sqlalchemy import Column, String,Integer

class Img(Base):
    __tablename__="img"

    id=Column(Integer,primary_key=True)
    path=Column(String(100))