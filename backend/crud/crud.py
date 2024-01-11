from sqlalchemy.orm import Session

from models.Img import Img
import schemas.Img as schemas

def get_imges(db:Session):
    return db.query(Img)

def add_imges(db:Session,img:schemas.Img):
    db_img=Img(path=img.path)
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img