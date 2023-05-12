import time, os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN, GROUP_ID, API_ID, API_HASH, USER_SESSION
from main.utils import progress_message, humanbytes


user = pyrogram.Client(
    "Userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    user_session=USER_SESSION)
    
    

@Client.on_message(filters.group & (filters.document | filters.video | filters.audio))         
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


@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot, msg):
    try:
        await msg.message.delete()
    except:
        return
    

@Client.on_callback_query(filters.regex('rename'))
async def rename(bot, msg):
    await msg.message.delete()
    await msg.message.reply_text("Enter New Filename...", reply_to_message_id = msg.message.reply_to_message.id, reply_markup=ForceReply(True))
    
    
    
@Client.on_message(filters.group & filters.reply)
async def refunc(bot, msg):
    reply_message = msg.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = msg.text
        cp_name = new_name + " " + "@SingleMachiOffl"
        get = await bot.get_messages(msg.chat.id, reply_message.id)
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
            await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Upload Started.....", sts, c_time))        
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
        
 
      
user.run()



