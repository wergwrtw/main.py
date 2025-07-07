import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # Flaskサーバー起動

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

SELF_INTRO_CHANNEL_ID = 1391324224823492702
ROLE_ID = 1391332661087174778

@bot.event
async def on_ready():
    print(f"✅ ログイン完了: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == SELF_INTRO_CHANNEL_ID:
        guild = message.guild
        role = discord.utils.get(guild.roles, id=ROLE_ID)
        if role:
            await message.author.add_roles(role)
            await message.channel.send(f"{message.author.mention} さんにロール「{role.name}」を付与しました！")
        else:
            await message.channel.send("❌ ロールが見つかりませんでした。")

    await bot.process_commands(message)

# Webサーバー起動（GAS用）
keep_alive()

# Bot起動
bot.run(TOKEN)
