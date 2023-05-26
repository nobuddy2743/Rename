import os, time
from config import Config
from CLINTON.module02 import progress, humanbytes

async def Xownload(bot, update, imog, app2, download_location):
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

    try:
        thumbnail = Config.THUMBNAIL + "/" + str(update.from_user.id) + ".jpg"
        if not os.path.isfile(thumbnail):
            thumbnail = None
    except Exception:
        thumbnail = None

    return thumbnail


async def Sthumload(bot, update, imog):

    try:
        incomings = update.photo.file_id
        thumbpath = Config.THUMBNAIL + "/" + str(update.from_user.id) + ".jpg"  
        await bot.download_media(message=incomings, file_name=thumbpath)
        await imog.edit(text="Thumbnail Saved ✅")
    except Exception as e:
        await imog.edit(text=f"<b>ERROR :</b> {e}")


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
