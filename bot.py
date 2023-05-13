from pyrogram import Client, idle
from config import *
import os
import time
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

from main.utils import progress_message, humanbytes

plugins = dict( root="main")
User_Session = "BABKlyIAshAUqAQUvB2Tu8e6itHrZzPdHUY3kBpUowO7ZqDpEZr5w6y3F4K4IrY9Zcfa3se5ubn85gUmv5STvxIlivAI83Kz3mtgVWaan7zNYzVDt8MoeUVH3nXXBH5GeaL6dWmh9ZmvdZ_3mvJgEuBxHBZ4L1Bpm3kuhnTqNERIztUZGcyTGhzaCFxRie1MEYLCe_qAq-llf_vF7MTTwf2jS0zWT9FPw6uhzQTOQRyKxxDgrrlr5Sk2NRv-69qFYGVwhMWkjCoEVBnaE4JllgosYIbi-DJ9BRgEngPs2eiUV_6YdqWcp7S8wbcK7XOtyuNMnh6JdiepKdzLyO-eGAsGnG3JUgAAAABpYAkOAA"


app1 = Client(
        "AnyDLBot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins)
        

app2 = Client(
        "Userbot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=User_Session)

@app1.on_message(filters.command('rn')  & filters.group & filters.reply)
async def rename(bot, message):
    reply = message.reply_to_message
    og_media = getattr(message, message.media.value)
    file_name = og_media.filename
    if message.chat.id == GROUP_ID:
        if reply and reply.media:
            sts = await bot.reply_text("Renaming...")
            new_name = file_name.split("-")[1]
            if not "." in new_name:
                cp_name = new_name + " " + "@SingleMachiOffl"
                f_name = cp_name + ".MKV"
            else:
                name = new_name.rsplit('.', 1)[-1]
                cp_name = name_name + " " + "@SingleMachiOffl"
                f_name = cp_name + ".MKV"
            c_time = time.time()
            downloaded = await app2.download(file_name=f_name, progress=progress_message, progress_args=("Downloading...", sts, c_time))  
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
                await app2.send_document(message.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Uploading..", sts, c_time))        
            except Exception as e:  
                return await sts.edit(f"Error {e}")                       
            try:
                if file_thumb:
                    os.remove(file_thumb)
                os.remove(downloaded)      
            except:
                pass
            await sts.delete()
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
    

    
print("i")

app1.start()
app2.start()
idle()
app1.stop()
app2.stop()
