

        try:

            c_time = time.time()

            downloaded = await app2.download_media(message=message.reply_to_message,

            file_name=file_name, progress=progress_message, progress_args=("Downloading...", imog, c_time))

        except Exception as e:

            await imog.edit(text=f"ERROR : {e}")

            retur
