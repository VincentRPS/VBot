import logging
import os
import pincer
from pincer import *
from pincer.objects import * # this isn't imported into normal pincer for some reason
from dotenv import load_dotenv

load_dotenv()

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

bot = pincer.Client(token=os.getenv("TOKEN"), intents=Intents.all())

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_cog(f"cogs.{filename[:-3]}")
        print(f"{filename[:-3]} Cog has loaded!")

@bot.event
async def on_ready():
    _log.info("Bot is now ready.")

bot.start_loop() # big brain me did this and it worked? bot.run won't work.