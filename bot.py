import os

import time
from config import Config
from pyrogram import Client, idle
from pyrogram import filters, enums
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
async def rename(bot, message):
    reply = message.reply_to_message
    file = await bot.get_messages(message.chat.id, reply.id)
    og_media = getattr(file, file.media.value)
    file_name = message.reply_to_message.caption
    if reply and reply.media:
        imog = await message.reply_text("Renaming...")
        new_name = file_name.split(" ", 1)[-1]
        caption_text = new_name + " " + "@SingleMachiOffl"
        try:
            c_time = time.time()
            downloaded = await app2.download_media(message=message.reply_to_message,
            file_name=file_name, progress=progress_message, progress_args=("Downloading...", imog, c_time))
        except Exception as e:
            await imog.edit(text=f"ERROR : {e}")
            return
        captions = str(caption_text)
        #thumb_path = works pending
        file_thumb = await bot.download_media(message=raw_thumb, file_name=thumb_path)
        await imog.edit("Trying to Upload")
        try:
            c_time = time.time()
            await app2.send_document(message.chat.id, document=downloaded, 
            thumb=og_thumbnail, caption=captions, progress=progress_message,
            progress_args=("Uploading...", imog, c_time))
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
