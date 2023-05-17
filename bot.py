from pyrogram import Client, idle
from config import Config
import os
import time
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

from main.utils import progress_message, humanbytes


app1 = Client(
        "AnyDLBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH)
        

app2 = Client(
        "Userbot",
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

       
        
@app1.on_message(filters.group & (filters.document | filters.video | filters.audio))         
async def rename_file(bot, msg):
    media = msg.document or msg.audio or msg.video
    og_media = getattr(msg, msg.media.value)
    filename = og_media.file_name
    filesize = humanbytes(og_media.file_size)
    text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
    buttons = [[ InlineKeyboardButton("𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴", callback_data="rename") ],
               [ InlineKeyboardButton("✖️", callback_data="cancel") ]]
    if msg.chat.id == GROUP_ID:
       return await msg.reply_text(text=text, reply_to_message_id=msg.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
       return 


@app1.on_callback_query(filters.regex('cancel'))
async def cancel(bot, msg):
    try:
        await msg.message.delete()
    except:
        return
    

@app1.on_callback_query(filters.regex('rename'))
async def rename(bot, msg):
    await msg.message.delete()
    await msg.message.reply_text("Enter New Filename...", reply_to_message_id = msg.message.reply_to_message.id, reply_markup=ForceReply(True))
    
    
    



@app1.on_message(filters.group & filters.reply)
async def refunc(bot, msg):
    reply_message = msg.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = msg.text
        cp_name = new_name + " " + "@SingleMachiOffl"
        get = await app2.get_messages(msg.chat.id, reply_message.id)
        file = get.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
        new_name = new_name + " " + "@SingleMachiOffl" +"." + "mkv"
        sts = await msg.reply_text("Trying to Downloading.....")
        c_time = time.time()
        downloaded = await file.download(file_name=new_name, progress=progress_message, progress_args=("Download Started.....", sts, c_time))  
        if CAPTION:
            try:
                cap = CAPTION.format(file_name=cp_name)
            except Exception as e:            
                return await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")           
        else:
            cap = f"{cp_name}"

        dir = os.listdir(DOWNLOAD_LOCATION)
        if len(dir) == 0:
            file_thumb = await bot.download_media(media.thumbs[0].file_id)
            og_thumbnail = file_thumb
        else:
            try:
                og_thumbnail = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
            except Exception as e:
                print(e)        
                og_thumbnail = None
        
        await sts.edit("Trying to Uploading")
        c_time = time.time()
        try:
            await app2.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Upload Started.....", sts, c_time))        
        except Exception as e:  
            return await sts.edit(f"Error {e}")                       
        try:
            if file_thumb:
                os.remove(file_thumb)
            os.remove(downloaded)      
        except:
            pass
        await sts.delete()
        await msg.delete()
        await reply_message.delete()
    

app1.start()
app2.start()
print("BOT STARTED 👶🏼")
idle()
app1.stop()
app2.stop()
print("BOT STOPPED 🌚")
