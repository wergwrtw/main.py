from flask import Flask, request
from threading import Thread
import os
import discord

app = Flask('')

@app.route('/')
def home():
    return "I'm alive", 200

@app.route('/ping')
def ping():
    return "pong", 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    message = data.get("content")

    if message:
        # Discordへ送信（Botが起動している必要あり）
        channel_id = int(os.environ.get("NOTIFY_CHANNEL_ID"))  # 通知用チャンネルIDを環境変数に
        loop = bot.loop  # main.pyでbotが定義されてる前提（同一スコープで定義が必要）

        async def send_msg():
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(message)

        loop.create_task(send_msg())

    return "ok", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
