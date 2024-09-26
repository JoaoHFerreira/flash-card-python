from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base



class LearningTopic(Base):
    __tablename__ = "learning_topic"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    flash_card = relationship("FlashCard", back_populates="learning_topic")



class FlashCard(Base):
    __tablename__ = "flash_card"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    learning_topic_id = Column(Integer, ForeignKey("learning_topic.id"), nullable=False)
    current_practice_day = Column(TIMESTAMP, nullable=False)
    next_practice_day = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    learning_topic = relationship("LearningTopic", back_populates="flash_card")
    historical_acceptances = relationship("HistoricalAcceptance", back_populates="flash_card")


class HistoricalAcceptance(Base):
    __tablename__ = "historical_acceptances"

    id = Column(Integer, primary_key=True, index=True)
    flash_card_id = Column(Integer, ForeignKey("flash_card.id"), nullable=False)
    answer_rate = Column(Integer, nullable=False)
    given_answer = Column(Text, nullable=False)
    test_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    flash_card = relationship("FlashCard", back_populates="historical_acceptances")
