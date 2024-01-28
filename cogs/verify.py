import discord
from discord.ext import commands
from discord.ui import View , Button



class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_verify_message(self, channel):
        channelid = self.bot.get_channel(channel)
        view = ReactionRole()
        await channelid.send("Please Verify Your Self", view=view)

    @commands.command()
    async def verify(self , ctx):
        channelid = ctx.channel.id
        await self.send_verify_message(channelid)


class ReactionRole(View):
    def __init__(self , * , timeout=None):
        super().__init__(timeout=None)


    @discord.ui.button(label="Subscribe", style=discord.ButtonStyle.red)
    async def subscribe(self , interaction: discord.Interaction , button:discord.ui.Button):
        if interaction.guild_id:
            role = interaction.guild.get_role(Role_ID)

            if role not in interaction.user.roles:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("You Get Verifyed Successfully")
            else:
                await interaction.response.send_message("You Already Have Valid Role")



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Verify(bot))