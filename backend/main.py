from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine,SessionLocal
from sqlalchemy.orm import Session
import schemas.Img as schemas
import models.Img as models
from crud.crud import get_imges,add_imges

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
def img_all(img:schemas.Img,db:Session=Depends(get_db)):
    imges=add_imges(db,img)
    return imges