from pyrogram import Client
from config import *
import os


class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()      
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       
    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")

    
user = Client(
        "Userbot",
        api_id="APP_ID",
        api_hash="API_HASH",
        user_session="BABKlyIAshAUqAQUvB2Tu8e6itHrZzPdHUY3kBpUowO7ZqDpEZr5w6y3F4K4IrY9Zcfa3se5ubn85gUmv5STvxIlivAI83Kz3mtgVWaan7zNYzVDt8MoeUVH3nXXBH5GeaL6dWmh9ZmvdZ_3mvJgEuBxHBZ4L1Bpm3kuhnTqNERIztUZGcyTGhzaCFxRie1MEYLCe_qAq-llf_vF7MTTwf2jS0zWT9FPw6uhzQTOQRyKxxDgrrlr5Sk2NRv-69qFYGVwhMWkjCoEVBnaE4JllgosYIbi-DJ9BRgEngPs2eiUV_6YdqWcp7S8wbcK7XOtyuNMnh6JdiepKdzLyO-eGAsGnG3JUgAAAABpYAkOAA")
       
bot = Bot()
bot.run()
user.run()
