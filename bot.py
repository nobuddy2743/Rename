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
       bot_token=Config.BOT_TOKEN)

app2 = Client("UBOT",
       api_id=Config.API_ID,
       api_hash=Config.API_HASH,
       session_string=Config.USESSION)


@app1.on_message(filters.command('rn')  & filters.group & filters.reply)
async def rename(bot, update):
    reply = update.reply_to_message
    file_name = message.reply_to_message.caption
    imog = await message.reply_text("Renaming...")
    new_name = file_name.split(" ", 1)[-1]
    captions = new_name + " " + "@SingleMachiOffl"
    fileoath = await Xownload(bot, update, imog, download_location)
    if fileoath == None:
        return
    #thumb_path = works pending
    file_thumb = await bot.download_media(message=raw_thumb, file_name=thumb_path)
    await imog.edit("Trying to Upload")
    try:
        ctime = time.time()
        await app2.send_document(message.chat.id, document=downloaded, 
        thumb=og_thumbnail, caption=captions, progress=progress_message,
        progress_args=("Uploading...", imog, ctime))
    except Exception as e:  
        os.remove(downloaded)
        await imog.edit(text=f"ERROR : {e}")   
        else:
            try:
                os.remove(downloaded)
            except:
                pass
            await imog.delete()
    else:
        await bot.send_message("It is fully automatic rename function.Reply with any file to rename")



app1.start()
app2.start()
print("BOT STARTED 👶🏼")
idle()
app1.stop()
app2.stop()
print("BOT STOPPED 🌚")
