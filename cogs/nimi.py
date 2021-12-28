from discord.ext import commands
from discord.commands import slash_command
from discord import Option
from discord import Embed
from discord import Colour
from discord import ButtonStyle
from discord.ui import View
from discord.ui import Button


from discord import context

from defines import text
import jasima

import re

class CogNimi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command(name="define", aliases=["d"])
        async def command_nimi(ctx, word):
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

    # regex the words! ouch
    word = re.sub(r"on", "õ", word)
    word = re.sub(r"un", "ũ", word)
    word = re.sub(r"oe", "ö", word)
    word = re.sub(r"ue", "ü", word)

    if re.match(r"\*\w*\*", word):
        word = word.strip("*")
        for i in word:
            if i == 'u':
                word = word.replace("u", "ú", 1)
                break
            if i == 'o':
                word = word.replace("o", "ó", 1)
                break

    elif re.match(r"~\w*~", word):
        word = word.strip("~")
        for i in word:
            if i == 'u':
                word = word.replace("u", "û", 1)
                break
            if i == 'o':
                word = word.replace("o", "ô", 1)
                break

    elif re.match(r">\w*<", word):
        word = word.strip(">")
        word = word.strip("<")
        for i in word:
            if i == 'u':
                word = word.replace("u", "ŭ", 1)
                break
            if i == 'o':
                word = word.replace("o", "ŏ", 1)
                break

    elif re.match(r"-\w*-", word):
        word = word.strip("-")
        for i in word:
            if i == 'u':
                word = word.replace("u", "ù", 1)
                break
            if i == 'o':
                word = word.replace("o", "ò", 1)
                break

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
