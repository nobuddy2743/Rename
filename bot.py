import os, time
import shutil, asyncio
from config import Config
from pyrogram import Client, idle
from pyrogram import filters, enums
from main.module01 import Xownload, Xpload, Sthumload
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

if not os.path.isdir(Config.DOWNLOADS):
    os.makedirs(Config.DOWNLOADS)
else:
    shutil.rmtree(Config.DOWNLOADS)
    os.makedirs(Config.DOWNLOADS)

if not os.path.isdir(Config.THUMBNAIL):
    os.makedirs(Config.THUMBNAIL)

#======================================================================================

@app1.on_message(filters.command('r')  & filters.group)
async def amname(bot, update):
    reply = update.reply_to_message
    file_name = str(update.reply_to_message.caption)
    imog = await update.reply_text("Renaming...")
    if file_name.startswith("www."):
        s_name = file_name.split(" ", 2)[-1]
    else:
        s_name = file_name
    if ".mkv" in s_name:
        new_name = s_name.replace(".mkv", " @SingleMachiOffl.mkv")
    else:
        new_name = s_name
    download_location = Config.DOWNLOADS + "/" + str(update.from_user.id) + "/"
    fileoath = await Xownload(bot, update, imog, app2, download_location)
    if fileoath == None:
        return
    newmedia_location = download_location + new_name
    os.rename(fileoath, newmedia_location)
    await imog.edit(text="Trying to Upload")
    await Xpload(bot, update, imog, app2, new_name, newmedia_location)

@app1.on_message(filters.private & filters.photo)
async def savethumb(bot, update):
    imog = await update.reply_text("Processing...")
    await Sthumload(bot, update, imog)


app1.start()
app2.start()
print("BOT STARTED 👶🏼")
idle()
app1.stop()
app2.stop()
print("BOT STOPPED 🌚")
