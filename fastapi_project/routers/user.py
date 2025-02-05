from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, hashing, database
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/user', tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/user/{id}', tags=['users'])
def get_user(id, response: Response, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    
    return user