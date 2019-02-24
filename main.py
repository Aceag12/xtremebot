import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp
from discord.utils import get
from discord.voice_client import VoiceClient
from random import choice, shuffle

commandprefix = "X!"

client = commands.Bot(command_prefix=commandprefix)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name="Xtreme's Videos", type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name="With Xtreme"))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    ...
    client.loop.create_task(status_task())   
    print('BOT_IS_ONLINE')

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★welcome-bye★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check #rules and never try to break any one of them. Thank You.', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url=member.avatar_url) 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★welcome-bye★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye! We will miss you..', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- **X!warn @user <reason>**')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say("***:white_check_mark: Alright! {0} Has Been Warned for {1}.*** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == 'server-logs':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await client.send_message(channel, embed=embed)
        else:
            return
        
client.run('NTQ3MDk0NjUzNTc3NDYxNzkw.D1QqOQ.rZMLwmh7w4ky1eZagmV7MghZ1mo')
