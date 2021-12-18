import logging
import os
import pincer
from pincer import *
from pincer.objects import * # this isn't imported into normal pincer for some reason
from dotenv import load_dotenv

load_dotenv()

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

bot = pincer.Client(token=os.getenv("TOKEN"), intents=Intents.all())

# TODO; get working cogs
"""
for cog in load.glob("cogs/*.py"):
    cog.replace("/", ".").replace("\\", ".")[:-3]"""
    
@bot.event
async def on_ready():
    _log.info("Bot is now ready.")

@command(description="The Ping of the bot")
async def ping(ctx: MessageContext):
    await ctx.send("Pong!")

bot.start_loop() # big brain me did this and it worked? bot.run won't work.