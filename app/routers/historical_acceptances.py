from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import HistoricalAcceptance as HistoricalAcceptanceModel
from schemas import HistoricalAcceptanceCreate, HistoricalAcceptanceUpdate, HistoricalAcceptance
from database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new historical acceptance
@router.post("/historical-acceptances/", response_model=HistoricalAcceptance)
def create_historical_acceptance(historical_acceptance: HistoricalAcceptanceCreate, db: Session = Depends(get_db)):
    db_historical_acceptance = HistoricalAcceptanceModel(**historical_acceptance.dict())
    db.add(db_historical_acceptance)
    db.commit()
    db.refresh(db_historical_acceptance)
    return db_historical_acceptance

# Get a historical acceptance by ID
@router.get("/historical-acceptances/{historical_acceptance_id}", response_model=HistoricalAcceptance)
def read_historical_acceptance(historical_acceptance_id: int, db: Session = Depends(get_db)):
    db_historical_acceptance = db.query(HistoricalAcceptanceModel).filter(HistoricalAcceptanceModel.id == historical_acceptance_id).first()
    if db_historical_acceptance is None:
        raise HTTPException(status_code=404, detail="Historical Acceptance not found")
    return db_historical_acceptance

# Get all historical acceptances
@router.get("/historical-acceptances/", response_model=List[HistoricalAcceptance])
def read_historical_acceptances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    historical_acceptances = db.query(HistoricalAcceptanceModel).offset(skip).limit(limit).all()
    return historical_acceptances

# Update a historical acceptance by ID
@router.put("/historical-acceptances/{historical_acceptance_id}", response_model=HistoricalAcceptance)
def update_historical_acceptance(historical_acceptance_id: int, historical_acceptance: HistoricalAcceptanceUpdate, db: Session = Depends(get_db)):
    db_historical_acceptance = db.query(HistoricalAcceptanceModel).filter(HistoricalAcceptanceModel.id == historical_acceptance_id).first()
    if db_historical_acceptance is None:
        raise HTTPException(status_code=404, detail="Historical Acceptance not found")
    for key, value in historical_acceptance.dict(exclude_unset=True).items():
        setattr(db_historical_acceptance, key, value)
    db.commit()
    db.refresh(db_historical_acceptance)
    return db_historical_acceptance

# Delete a historical acceptance by ID
@router.delete("/historical-acceptances/{historical_acceptance_id}")
def delete_historical_acceptance(historical_acceptance_id: int, db: Session = Depends(get_db)):
    db_historical_acceptance = db.query(HistoricalAcceptanceModel).filter(HistoricalAcceptanceModel.id == historical_acceptance_id).first()
    if db_historical_acceptance is None:
        raise HTTPException(status_code=404, detail="Historical Acceptance not found")
    db.delete(db_historical_acceptance)
    db.commit()
    return {"detail": "Historical Acceptance deleted successfully"}