from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from config import Config
from utils.storage import UserStorage

app = FastAPI()
config = Config()
storage = UserStorage()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<html><body><h1>Codex2050 Dashboard</h1><p>Status: Online</p></body></html>"

@app.get("/api/stats")
async def stats():
    return storage.get_system_stats()

async def start_web_server():
    config_obj = uvicorn.Config(app, host=config.WEB_HOST, port=config.WEB_PORT, log_level="info")
    server = uvicorn.Server(config_obj)
    await server.serve()
