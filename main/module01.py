import os, time
from config import Config
from main.module02 import progress, humanbytes

async def Xownload(bot, update, imog, download_location):
    try:
        ctime = time.time()
        file_location = await bot.download_media(
        message=update.reply_to_message,
        file_name=download_location,
        progress=progress,
        progress_args=("Downloading...", imog, ctime))
    except Exception as e:
        await imog.edit(text=f"ERROR : {e}")
        file_location = None

    return file_location


async def Townload(bot, update):

    if update.from_user.id == 1477582805:
        rawthumbs = "AgACAgUAAxkBAAENi4xkZgYg0VPu8MfClzvc-elXDRneugACXbYxG61TqVbEY1hb9_UHawEAAwIAA3kAAy8E"
    else:
        rawthumbs = "AgACAgUAAxkBAAENi49kZgZkQkJy5xphV4LMbve8tvXZgwACF7QxG6Z0-FRWEf5UF891hgEAAwIAA3gAAy8E"
    try:
        thumbpath = Config.DOWNLOADS + "/" + str(update.from_user.id) + ".jpg"  
        thumbnail = await bot.download_media(message=rawthumbs, file_name=thumbpath)
    except Exception:
        thumbnail = None

    return thumbnail


async def Xpload(bot, update, imog, client, captions, file_location):

    thumbnail = await Townload(bot, update)
    try:
        ctime = time.time()
        await client.send_document(chat_id=update.chat.id, document=file_location, 
        thumb=thumbnail, caption=captions, progress=progress,
        progress_args=("Uploading...", imog, ctime))
        await imog.delete(True)
    except Exception as e:
        await imog.edit(text=f"ERROR : remove{e}")
    
    await cleanord(file_location)
    
    

async def cleanord(filesz):
    try:
        os.remove(filesz)
    except Exception:
        pass
