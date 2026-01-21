# Telegram Bot Flask API

🤖 A Flask-based API wrapper for a Telegram bot with AI integration.

## Features

- ✅ Flask API with webhook support
- ✅ Telegram bot commands (`/start`, `/ask`, `/help`, `/admin`, `/live`)
- ✅ AI-powered responses via external API
- ✅ Webhook and polling mode support
- ✅ Health check endpoint
- ✅ Easy deployment to Render, Railway, or Heroku

## Commands

- `/start` - Welcome message and command list
- `/ask <question>` - Get AI-generated response
- `/help` - Get support information
- `/admin` - View admin contact
- `/live` - View chat information

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Stiphan680/telegram-bot-flask-api.git
cd telegram-bot-flask-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token_here
MODE=webhook
PORT=5000
```

### 4. Run locally

**Polling Mode (for local development):**

```bash
export MODE=polling
python app.py
```

**Webhook Mode (for production):**

```bash
export MODE=webhook
python app.py
```

## Deployment

### Deploy to Render

1. Push code to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Connect your repository
4. Set environment variables:
   - `BOT_TOKEN`: Your Telegram bot token
   - `MODE`: `webhook`
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn app:app`
7. Deploy!

### Set Webhook

After deployment, set your webhook:

```
https://your-app-url.onrender.com/set_webhook?url=https://your-app-url.onrender.com
```

## API Endpoints

### `GET /`
Home endpoint with API information

**Response:**
```json
{
  "status": "online",
  "message": "Telegram Bot Flask API is running",
  "endpoints": {...}
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "bot_username": "YourBotUsername"
}
```

### `POST /webhook`
Webhook endpoint for Telegram updates (automatically called by Telegram)

### `GET /set_webhook?url=YOUR_URL`
Set webhook URL for the bot

**Parameters:**
- `url`: Your deployed application URL

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram bot token from @BotFather | Yes |
| `MODE` | `webhook` or `polling` | No (default: webhook) |
| `PORT` | Port to run the Flask app | No (default: 5000) |

## Technologies Used

- **Flask** - Web framework
- **pyTelegramBotAPI** - Telegram bot library
- **Gunicorn** - WSGI HTTP Server
- **Requests** - HTTP library

## Getting Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions
4. Copy your bot token

## License

MIT License

## Support

For support, contact [@NGYT777GG](https://t.me/NGYT777GG) on Telegram.

## Author

Admin: @GOAT_NG