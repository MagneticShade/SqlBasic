from fastapi import FastAPI,Depends,UploadFile,HTTPException
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine,SessionLocal
from sqlalchemy.orm import Session
import schemas.Img as schemas
import models.Img as models
from crud.crud import get_imges,add_imges
import re

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close

@app.get('/',response_model=list[schemas.Img])
def img_all(db:Session=Depends(get_db)):
    imges=get_imges(db)
    return imges

@app.post('/',response_model=schemas.Img)
def img_all(file:UploadFile,db:Session=Depends(get_db)):
    size = len(file.file.read())
    if(file.content_type == "image/png" and size<=(3*1024*1024)):
        tmp=re.sub(".*/","",file.filename)
        print (tmp)
        img=schemas.Img(path=tmp)
        imges=add_imges(db,img)
        return imges
    raise HTTPException(status_code=413)
    