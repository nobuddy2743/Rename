import os

import time
from config import Config
from pyrogram import Client, idle
from pyrogram import filters, enums
from main.module01 import Xownload
from main.utils import progress_message, humanbytes
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

app1 = Client("RBOT",
       api_id=Config.API_ID,
       api_hash=Config.API_HASH,
       bot_token=Config.BOT_TOKEN,
       parse_mode=enums.ParseMode.HTML)

app2 = Client("UBOT",
       api_id=Config.API_ID,
       api_hash=Config.API_HASH,
       session_string=Config.USESSION,
       parse_mode=enums.ParseMode.HTML)

#======================================================================================

@app1.on_message(filters.command('rn')  & filters.group)
async def amname(bot, update):
    reply = update.reply_to_message
    file_name = message.reply_to_message.caption
    imog = await message.reply_text("Renaming...")
    new_name = file_name.split(" ", 1)[-1]
    captions = new_name + " " + "@SingleMachiOffl"
    fileoath = await Xownload(bot, update, imog, download_location)
    if fileoath == None:
        return
    await imog.edit(text="Trying to Upload")
    # UPLOADER ------ SOON

app1.start()
app2.start()
print("BOT STARTED 👶🏼")
idle()
app1.stop()
app2.stop()
print("BOT STOPPED 🌚")
