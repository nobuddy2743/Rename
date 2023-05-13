from pyrogram import Client
from config import *
import os


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


    

    
print("i")

app1.run()
app2.run()
