import logging
import waifuim
from pincer import *
from pincer.objects import *

_log = logging.getLogger(__name__)

wc = waifuim.WaifuAioClient()

class Waifu:

    @command(description="Get a waifu", guild="906815360492253205")
    async def waifu(self, ctx: MessageContext):
        waifu = await wc.sfw("waifu", many=False)
        await ctx.send(f"{waifu}")
        _log.info("Waifu command was used")
    
    @command(description="Get a maid waifu", guild="906815360492253205")
    async def maid(self, ctx: MessageContext):
        waifu = await wc.sfw("maid", many=False)
        await ctx.send(f"{waifu}")
        _log.info("Maid command was used")

setup = Waifu