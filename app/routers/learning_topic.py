from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import LearningTopic as LearningTopicModel
from schemas import LearningTopic, LearningTopicCreate
from database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new learning topic
@router.post("/learning_topic/", response_model=LearningTopic)
def create_learning_topic(learning_topic: LearningTopicCreate, db: Session = Depends(get_db)):
    db_learning_topic = LearningTopicModel(**learning_topic.dict())
    db.add(db_learning_topic)
    db.commit()
    db.refresh(db_learning_topic)
    return db_learning_topic

# Get all learning topics
@router.get("/learning_topic/", response_model=List[LearningTopic])
def get_learning_topics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    learning_topics = db.query(LearningTopicModel).offset(skip).limit(limit).all()
    return learning_topics

# Get a specific learning topic by ID
@router.get("/learning_topic/{topic_id}", response_model=LearningTopic)
def get_learning_topic(topic_id: int, db: Session = Depends(get_db)):
    learning_topic = db.query(LearningTopicModel).filter(LearningTopicModel.id == topic_id).first()
    if not learning_topic:
        raise HTTPException(status_code=404, detail="Learning topic not found")
    return learning_topic

# Update a learning topic
@router.put("/learning_topic/{topic_id}", response_model=LearningTopic)
def update_learning_topic(topic_id: int, updated_topic: LearningTopicCreate, db: Session = Depends(get_db)):
    learning_topic = db.query(LearningTopicModel).filter(LearningTopicModel.id == topic_id).first()
    if not learning_topic:
        raise HTTPException(status_code=404, detail="Learning topic not found")
    
    learning_topic.subject = updated_topic.subject
    db.commit()
    db.refresh(learning_topic)
    return learning_topic

# Delete a learning topic
@router.delete("/learning_topic/{topic_id}", response_model=LearningTopic)
def delete_learning_topic(topic_id: int, db: Session = Depends(get_db)):
    learning_topic = db.query(LearningTopicModel).filter(LearningTopicModel.id == topic_id).first()
    if not learning_topic:
        raise HTTPException(status_code=404, detail="Learning topic not found")
    
    db.delete(learning_topic)
    db.commit()
    return learning_topic
