from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Schema for creating a new learning topic
class LearningTopicCreate(BaseModel):
    subject: str

# Schema for reading LearningTopic, with optional flash_cards
class LearningTopic(BaseModel):
    id: int
    subject: str
    created_at: datetime
    flash_cards: Optional[List["FlashCard"]] = None  # Optional relationship with flashcards

    class Config:
        orm_mode = True


class FlashCardBase(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None

class FlashCardCreate(FlashCardBase):
    pass

class FlashCardUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None

class FlashCard(FlashCardBase):
    id: int

    class Config:
        orm_mode = True


class HistoricalAcceptanceBase(BaseModel):
    flash_card_id: int
    answer_rate: int
    given_answer: str
    test_date: datetime

class HistoricalAcceptanceCreate(HistoricalAcceptanceBase):
    pass

class HistoricalAcceptanceUpdate(BaseModel):
    answer_rate: Optional[int] = None
    given_answer: Optional[str] = None
    test_date: Optional[datetime] = None

class HistoricalAcceptance(HistoricalAcceptanceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True