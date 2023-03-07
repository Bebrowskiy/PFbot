import disnake
from time import time
import datetime
#from pypresence import Presence
from disnake.ext import commands

from Cybernator import Paginator as pag
import asyncio
import config

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

@bot.event
async def on_ready():
	print("Bot ready")
"""
@bot.command()
@commands.has_permissions(administrator=True)
async def tmute(ctx, member: disnake.Member = None, time: str = None, *, reason="Нарушение правил сервера"):
	if member is None:
		return await ctx.send("Укажите участника!")
	if member.bot is True:
		return await ctx.send("Вы не можете замутить **бота**!")
	if time is None:
		return ctx.send("Укажите время мута!")
	else:
		try:
			seconds = int(time[:-1])
			duraction = time[-1]
			if duraction == "s":
				pass
			if duraction == "m":
				seconds *= 60
			if duraction == "h":
				seconds *= 3600
			if duraction == "d":
				seconds *= 86400
		except:
			return await ctx.send("Указано неверное время мута")
		mute_expiration = (datetime.datetime.now() + datetime.timedelta(seconds=int(seconds))).strftime("%c")
"""

@bot.command()
@commands.has_permissions(administrator=True)
async def tempmute(ctx, member: disnake.Member = None, time: int = None, reason="Нарушение правил сервера"):
	if member == None:
		return await ctx.send("Укажите участника!")
	if time == None:
		return await ctx.send("Укажите время мута в секундах!")
	else:
		await ctx.channel.purge(limit=2)

		await ctx.send(f"{ctx.author.mention} замутил {member.mention} на {time} секунд по причине: {reason}")

		guild = bot.get_guild(1072575907153330316)
		role = guild.get_role(1072585167312519218)
		await member.add_roles(role)

		await asyncio.sleep(time) # Спим X секунд, перед тем как снять роль. 
		await member.remove_roles(role)
   	 # Снимаем роль замученного.

bot.run("OTQzMDAwMjUyOTQ3MDAxNDY1.Gk9fRm.UKpJeBrwPwRgSTE3LCkE0USwcjy3alQJXrosuA")