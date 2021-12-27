from discord.ext import commands
from discord.commands import slash_command
from discord import Option
from discord import Embed
from discord import Colour
from discord import ButtonStyle
from discord.ui import View
from discord.ui import Button

from keep_alive import keep_alive


from discord import context

from defines import text
import jasima

class CogNimi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command(name="d")
        async def command_nimi(ctx, word):
            if word.startswith("word:"):
                word = word.replace("word:", "", 1)
            await nimi(ctx, word)
        @bot.command(name="define")
        async def command_n(ctx, word):
            if word.startswith("word:"):
                word = word.replace("word:", "", 1)
            await nimi(ctx, word)

    @slash_command(
      name='d',
      description=text["DESC_NIMI"],
    )
    async def slash_nimi(self, ctx, word: Option(str, text["DESC_NIMI_OPTION"])):
        await nimi(ctx, word)

    @slash_command(
      name='define',
      description=text["DESC_NIMI"],
    )
    async def slash_n(self, ctx, word: Option(str, text["DESC_NIMI_OPTION"])):
        await nimi(ctx, word)

async def nimi(ctx, word):

    response = jasima.get_word_entry(word)
    if isinstance(response, str):
        if isinstance(ctx, context.ApplicationContext):
            await ctx.respond(response)
        else:
            await ctx.send(response)
        return
    embed = embed_response(word, response)
    if isinstance(ctx, context.ApplicationContext):
        await ctx.respond(embed=embed)
    else:
        await ctx.send(embed=embed)

def embed_response(word, response):
    embed = Embed()
    embed.title = response["word"]
    embed.colour = Colour.from_rgb(247,168,184)
    for i in response["def"].keys():
        embed.add_field(name=i, value=response["def"][i])

    return embed
