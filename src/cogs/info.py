import logging
from pincer import *
from pincer.objects import *

_log = logging.getLogger(__name__)

class Info:
    """Info, /ping /info /help etc."""

    @command(description="The Ping of the bot")
    async def ping(self, ctx: MessageContext):
        await ctx.send("Pong!")
        _log.info("Ping command was used")

setup = Info