from flask import Flask, request, jsonify
import telebot
import requests
import os
from threading import Thread

app = Flask(__name__)

# Configuration
TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
API_URL = "https://nggemini.tiiny.io/?prompt="

bot = telebot.TeleBot(TOKEN)

# Start Command
@bot.message_handler(commands=["start"])
def start(message):
    text = "👋 Welcome! Use the following commands:\n\n"
    text += "🔹 /ask - Get AI-generated response\n"
    text += "🔹 /help - Get support\n"
    text += "🔹 /admin - Contact Admin\n"
    text += "🔹 /live - View live members count"
    bot.send_message(message.chat.id, text)

# Ask Command (Fetch from API)
@bot.message_handler(commands=["ask"])
def ask(message):
    query = message.text.replace("/ask", "").strip()
    if not query:
        bot.send_message(message.chat.id, "❌ Please enter a question after /ask")
        return
    
    try:
        response = requests.get(API_URL + query, timeout=30)
        bot.send_message(message.chat.id, "🤖 AI Response:\n" + response.text)
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {str(e)}")

# Help Command
@bot.message_handler(commands=["help"])
def help_command(message):
    text = "Need help? Click below to DM me 👇"
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("💬 Contact Developer", url="https://t.me/NGYT777GG"))
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# Admin Command
@bot.message_handler(commands=["admin"])
def admin(message):
    bot.send_message(message.chat.id, "👤 Admin: @GOAT_NG")

# Live Command (Show Bot Members Count)
@bot.message_handler(commands=["live"])
def live(message):
    try:
        bot_info = bot.get_me()
        chat_info = bot.get_chat(message.chat.id)
        bot.send_message(message.chat.id, f"📊 Chat ID: {chat_info.id}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Error: {str(e)}")

# Flask Routes
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Telegram Bot Flask API is running",
        "endpoints": {
            "/webhook": "POST - Webhook endpoint for Telegram",
            "/set_webhook": "GET - Set webhook URL",
            "/health": "GET - Health check"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "bot_username": bot.get_me().username})

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming updates from Telegram"""
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return jsonify({"status": "ok"})
    else:
        return jsonify({"error": "Invalid content type"}), 403

@app.route('/set_webhook')
def set_webhook():
    """Set webhook URL for the bot"""
    webhook_url = request.args.get('url')
    if not webhook_url:
        return jsonify({"error": "Please provide webhook URL as ?url=YOUR_URL"}), 400
    
    try:
        bot.remove_webhook()
        success = bot.set_webhook(url=webhook_url + '/webhook')
        if success:
            return jsonify({"status": "success", "webhook_url": webhook_url + '/webhook'})
        else:
            return jsonify({"status": "failed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run in polling mode for local development
def run_bot():
    bot.remove_webhook()
    bot.infinity_polling()

if __name__ == '__main__':
    # For local development with polling
    mode = os.getenv('MODE', 'webhook')
    
    if mode == 'polling':
        # Run bot in polling mode in a separate thread
        Thread(target=run_bot, daemon=True).start()
    
    # Run Flask app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)