from discord.ext import commands

from keep_alive import keep_alive

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

from cogs.nimi import CogNimi

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("* {}".format(guild.name))

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == bot.user:
        if reaction.emoji == "❌":
            await reaction.message.delete()

if __name__ == "__main__":
    bot.add_cog(CogNimi(bot))
    keep_alive()
    bot.run(TOKEN, reconnect=True)

