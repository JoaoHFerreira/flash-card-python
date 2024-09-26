from fastapi import FastAPI
from routers import learning_topic, historical_acceptances, flash_cards
from database import init_db

app = FastAPI()
init_db()

app.include_router(learning_topic.router)
app.include_router(historical_acceptances.router)
app.include_router(flash_cards.router)