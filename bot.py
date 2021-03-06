import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents = intents)

token = 'NzY0OTEyNDY2NDgwMDcwNjY5.X4NKPw.XWVY_geulGVDbItWGrkDmoRCm94'

@client.event
async def on_ready():
	print('Bot is ready.')

@client.event
async def on_member_join(member):
	print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
	print(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
	responses =	["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')	



client.run(token)