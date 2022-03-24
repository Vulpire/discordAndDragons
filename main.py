import discord
from discord_slash import SlashCommand
from random import random
from discord_slash.utils.manage_commands import create_option
from multipledispatch import dispatch

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

guild_ids = [342146742399139853, 600407836794814506, 754505878123839619]


@client.event
async def on_ready():
    print("Bot ready")


# displays the users pfp
@slash.slash(name="mypfp", description="Displays your pfp", guild_ids=guild_ids)
async def pfp(ctx):

    embed = discord.Embed(
        title=f"Avatar of {ctx.author.display_name}",
        color=discord.Colour.teal()
    ).set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


# dice rolling command
@slash.slash(name="roll",
             description="This command rolls some dice",
             guild_ids=guild_ids,
             options=[
               create_option(
                 name="dienumber",
                 description="which type of die would you like to roll.",
                 option_type=4,
                 required=True
               ),
               create_option(
                 name="numberofdie",
                 description="how many would you like to roll",
                 option_type=4,
                 required=False
                )
             ])
async def roll(ctx, dienumber: int):
    rollNum = round(random() * dienumber)
    await ctx.send(f"{ctx.author.display_name} rolled a {rollNum}")


async def roll(ctx, dienumber: int, numberofdie: int):
    rollNum = round(random() * dienumber) + 1
    await ctx.send(f"{ctx.author.display_name} rolled a {rollNum}")


# clears chat
@slash.slash(name="clear", description="clears a number of messages", guild_ids=guild_ids)
async def clear(ctx, *, number):
    if number.isnumeric():
        async for message in ctx.channel.history(limit=int(number)):
            await message.delete()
        await ctx.send(f"{number} messages have been deleted")
    else:
        await ctx.send("Please enter a valid number")
@client.event
async def on_message(message):
    if message.author == client.user: #spiderman meme
        return
    else:
      #allows bot to respond to specific messages
        return
        
client.run(token)