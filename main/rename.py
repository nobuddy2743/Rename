import time, os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN, GROUP_ID
from main.utils import progress_message, humanbytes


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
    
    
    



