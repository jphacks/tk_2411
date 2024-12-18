from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.diary import diary_router
from app.routes.line_bot import line_bot_router
from app.routes.user_profile import user_router

app = FastAPI()

app.include_router(diary_router)
app.include_router(user_router)
app.include_router(line_bot_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
