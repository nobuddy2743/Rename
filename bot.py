import os, time, asyncio
from config import Config
from pyrogram import Client, idle
from pyrogram import filters, enums
from main.module01 import Xownload, Xpload
from main.module02 import progress, humanbytes
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
    new_name = file_name.split(" ", 1)[-1] + ".mkv"
    download_location = Config.DOWNLOAD + "/" + str(update.from_user.id) + "/" + file_name
    fileoath = await Xownload(bot, update, imog, download_location)
    if fileoath == None:
        return
    os.rename(download_location, 
    await imog.edit(text="Trying to Upload")
    asyncio.create_task(Xpload(bot, update, imog, client, new_name, fileoath))

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
