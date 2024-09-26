from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import FlashCard as FlashCardModel
from schemas import FlashCardCreate, FlashCardUpdate, FlashCard
from database import SessionLocal
from typing import List

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new flashcard
@router.post("/flashcards/", response_model=FlashCard)
def create_flashcard(flashcard: FlashCardCreate, db: Session = Depends(get_db)):
    db_flashcard = FlashCardModel(**flashcard.dict())
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

# Get a flashcard by ID
@router.get("/flashcards/{flashcard_id}", response_model=FlashCard)
def read_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    db_flashcard = db.query(FlashCardModel).filter(FlashCardModel.id == flashcard_id).first()
    if db_flashcard is None:
        raise HTTPException(status_code=404, detail="FlashCard not found")
    return db_flashcard

# Get all flashcards
@router.get("/flashcards/", response_model=List[FlashCard])
def read_flashcards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flashcards = db.query(FlashCardModel).offset(skip).limit(limit).all()
    return flashcards

# Update a flashcard by ID
@router.put("/flashcards/{flashcard_id}", response_model=FlashCard)
def update_flashcard(flashcard_id: int, flashcard: FlashCardUpdate, db: Session = Depends(get_db)):
    db_flashcard = db.query(FlashCardModel).filter(FlashCardModel.id == flashcard_id).first()
    if db_flashcard is None:
        raise HTTPException(status_code=404, detail="FlashCard not found")

    for key, value in flashcard.dict(exclude_unset=True).items():
        setattr(db_flashcard, key, value)

    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

# Delete a flashcard by ID
@router.delete("/flashcards/{flashcard_id}")
def delete_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    db_flashcard = db.query(FlashCardModel).filter(FlashCardModel.id == flashcard_id).first()
    if db_flashcard is None:
        raise HTTPException(status_code=404, detail="FlashCard not found")
    
    db.delete(db_flashcard)
    db.commit()
    return {"detail": "FlashCard deleted successfully"}
