import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_message(message):
    if message.author.id == 832968969463005194:
        return
    if message.guild.id == 832970125648855041:
        if message.channel == 832970126264893452:
            await message.channel.send("@everyone")

bot.run("ODMyOTY4OTY5NDYzMDA1MTk0.YHrgzg.e6t5_-MaovKxhFfWEmLFWdKZkzo")