# Codex2050

Telegram bot powered by DeepSeek AI with optional web dashboard and RPC endpoints.

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

## Deployment
Render configuration (`render.yaml`) references secret environment variables. Keep your TELEGRAM_TOKEN and DEEPSEEK_API_KEY in Render's dashboard; they are not stored in the repository.

### Render secrets
- Secrets such as `TELEGRAM_TOKEN` and `DEEPSEEK_API_KEY` stay in Render's Environment Variables page (already set up in the dashboard screenshot) and are **not** checked into git.
- If you need to rotate or review a value, open the Render dashboard, edit the corresponding key, and redeploy—no code changes are required.
