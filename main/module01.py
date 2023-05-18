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
