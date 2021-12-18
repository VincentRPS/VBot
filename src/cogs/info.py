import logging
from pincer import *
from pincer.objects import * # TODO; clear the import crisis here.

_log = logging.getLogger(__name__)

class Info:
    """Info, /ping /info /help etc."""
    @command(description="The Ping of the bot", guild="917761976141238282")
    async def ping(self, ctx: MessageContext):
        await ctx.send("Pong!")

setup = Info