import os, time, asyncio
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

#======================================================================================

@app1.on_message(filters.command('rn')  & filters.group)
async def amname(bot, update):
    reply = update.reply_to_message
    file_name = update.reply_to_message.caption
    imog = await update.reply_text("Renaming...")
    new_name = file_name.split(" ", 2)[-1]
    download_location = Config.DOWNLOADS + "/" + str(update.from_user.id) + "/"
    fileoath = await Xownload(bot, update, imog, download_location)
    if fileoath == None:
        return
    newmedia_location = download_location + new_name
    os.rename(fileoath, newmedia_location)
    await imog.edit(text="Trying to Upload")
    await Xpload(bot, update, imog, app2, new_name, newmedia_location)

@app1.on_message(filters.photo)
async def savethumb(bot, update):
    await Sthumload(bot, update)

app1.start()
app2.start()
if not os.path.isdir(Config.DOWNLOADS):
    os.makedirs(Config.DOWNLOADS)
else:
    shutil.rmtree(Config.DOWNLOADS)
    os.makedirs(Config.DOWNLOADS)
print("BOT STARTED 👶🏼")
idle()
app1.stop()
app2.stop()
print("BOT STOPPED 🌚")
