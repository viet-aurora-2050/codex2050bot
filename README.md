# Codex2050

Telegram bot powered by DeepSeek AI with optional RPC endpoints.

## Setup
1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy the sample environment file and fill in your private tokens (never commit them):
   ```bash
   cp .env.example .env
   # edit .env to add TELEGRAM_TOKEN and any other overrides
   ```
3. Start the bot locally:
   ```bash
   python main.py
   ```

Optional: If you want to enable the optional web dashboard, set `ENABLE_WEB=true` in your `.env` **and** install the web extras:
```bash
pip install fastapi uvicorn
```

## Deployment
Render configuration (`render.yaml`) references secret environment variables. Keep your TELEGRAM_TOKEN and DEEPSEEK_API_KEY in Render's dashboard; they are not stored in the repository. The dashboard service is disabled by default to avoid FastAPI/uvicorn dependencies; enable it only if you deploy your own web UI.

### Render secrets
- Secrets such as `TELEGRAM_TOKEN` and `DEEPSEEK_API_KEY` stay in Render's Environment Variables page (already set up in the dashboard screenshot) and are **not** checked into git.
- If you need to rotate or review a value, open the Render dashboard, edit the corresponding key, and redeploy—no code changes are required.

## Render-Deployment neu aufsetzen (Cache-freier Restart)
Falls Render nach mehreren Versuchen noch fehlerhafte Builds oder alte Caches nutzt, hilft ein kompletter Neu-Deploy über GitHub:

1. **Neues GitHub-Repo anlegen** (Name z. B. `codex2050bot`) und den aktuellen Projektstand ohne Unterordner in das Root-Verzeichnis pushen. Wichtige Dateien, die im Repository-Wurzelverzeichnis liegen müssen: `main.py`, `requirements.txt`, `render.yaml` und der `Procfile` mit `worker: python main.py`.
2. **Render-Service neu erstellen**: „New Web Service“ → GitHub-Repo wählen → Runtime Python 3.11 → Build Command leer lassen oder `pip install -r requirements.txt` → Start Command `python main.py` (dient hier als Worker). Das Dashboard bleibt optional (ENV `ENABLE_WEB=false`).
3. **Build-Cache leeren**: In Render unter *Advanced* → *Clear build cache* wählen, dann *Manual Deploy → Deploy latest commit* auslösen.
4. **Secrets prüfen**: TELEGRAM_TOKEN und DEEPSEEK_API_KEY im Render-Dashboard hinterlegen (nicht im Code). Danach neu deployen.

Damit erhält Render eine saubere Basis ohne veraltete Buildpack-/Cache-Artefakte, und der Bot startet direkt über den Worker-Prozess.
