import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id=Bot_ID,
            case_insensitive=True
        )
    
        self.bot_cogs = ["cogs.verify"]
    
    async def setup_hook(self):
        for cogs in self.bot_cogs:
            await self.load_extension(cogs)
        await self.tree.sync()
        print("Successfully setup for {0}".format(self.user))

bot = MyBot()
bot.remove_command("help")



bot.run(Bot_Token)