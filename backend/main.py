from fastapi import FastAPI,Depends,UploadFile,HTTPException,File
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine,SessionLocal
from sqlalchemy.orm import Session
import schemas.Img as schemas
import models.Img as models
from crud.crud import get_imges,add_imges
import re
import shutil
from os import path

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
    file_content=file.file.read()
    size = len(file_content)
    if(file.content_type == "image/png"):

        if( size<=(3*1024*1024)):
            pure_name=re.sub(".*/","",file.filename)
            
            img=schemas.Img(path=pure_name)
            imges=add_imges(db,img)
            basepath = path.dirname(__file__)
            file_location = path.abspath(path.join(basepath, "..","frontend","frontend","public", pure_name ))

            with open(file_location, "wb+") as file_object:
                file_object.write(file_content)
                
            return imges
        raise HTTPException(status_code=413)
    
    raise HTTPException(status_code=412)
    