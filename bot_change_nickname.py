import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

user_process = {}
@bot.command(pass_context=True)
async def samnick(ctx, member: discord.Member):
    id = member._user.id
    user_process.pop(id, None)

@bot.command(pass_context=True)
async def amnick(ctx, member: discord.Member, text):
    id = member._user.id
    if user_process.get(id, False):
        return
    user_process[id] = True
    name = text
    i = 0
    while user_process.get(id, False):
        new_name = name + '.' * (i+1)
        await member.edit(nick=new_name)
        i = (i + 1)%3
        time.sleep(0.2)
    # await ctx.send(f'Nickname was changed for {member.mention} ')
print("Start bot")
f = open('token.txt')
token = f.readline()
f.close()
bot.run(token)
