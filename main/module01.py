import time

async def Xownload(bot, update, imog, download_location):
    try:
        ctime = time.time()
        file_location = await bot.download_media(
        message=update.reply_to_message,
        file_name=download_location,
        progress=progress_message,
        progress_args=("Downloading...", imog, ctime))
    except Exception as e:
        await imog.edit(text=f"ERROR : {e}")
        file_location = None

    return file_location


async def Townload(bot, update):
    
    try:
        rawthumbs = "https://telegra.ph/file/af87abd20b30953a71a91.jpg"
        thumbpath = Config.DOWNLOADS + "/" + str(update.from_user.id) + ".jpg"  
        thumbnail = await bot.download_media(message=rawthumbs, file_name=thumbpath)
    except Exception:
        thumbnail = None

    return thumbnail
