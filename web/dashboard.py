import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from telegram import Update
from telegram.ext import Application

from config import Config
from utils.storage import UserStorage

app = FastAPI()
config = Config()
storage = UserStorage()

telegram_app = Application.builder() \
    .token(os.environ["TELEGRAM_TOKEN"]) \
    .build()


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<html><body><h1>Codex2050 Dashboard</h1></body></html>"


@app.get("/api/stats")
async def stats():
    return storage.get_system_stats()


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}
