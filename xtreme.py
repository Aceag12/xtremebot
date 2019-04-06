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
from random import choice, shuffle
import logging
 
client = commands.Bot(description="ExtremeModerator Is Awesome", command_prefix=commands.when_mentioned_or("E." ,"e."))
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='E.help | e.help', url='https://twitch.tv/streamer', type=1))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' Servers', url='https://twitch.tv/streamer', type=1))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name='for '+str(len(set(client.get_all_members())))+' Members', url='https://twitch.tv/streamer', type=1))
        await asyncio.sleep(15)

@client.event
async def on_ready():
    print('the bot is ready')
    print(client.user.name)
    print(client.user.id)
    print('working properly')
    client.loop.create_task(status_task())

@client.command(pass_context = True)
async def setlogs(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command.**')
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=False)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '〚📑〛extreme-logs',everyone)
      await client.say('〚📑〛extreme-logs channel has been created.')

@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
        return
    else:    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='HELP CENTER OF EXTREMEMODERATOR BOT')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name = '__**COMING SOON:**__',value ='`COMING SOON!`',inline = False)
        embed.set_footer(text ='CREATED BY ALISTORM||ASH KETCHUM')
        await client.say(embed=embed)

@client.event
async def on_message_edit(before, after):
    if before.content == after.content:
      return
    if before.author == client.user:
      return
    else:
      user = before.author
      member = after.author
      for channel in user.server.channels:
        if channel.name == '〚📑〛extreme-logs':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Message edited')
            embed.add_field(name = 'UserName:',value ='**{}**'.format(user),inline = False)
            embed.add_field(name = 'User ID:',value ='**{}**'.format(user.id),inline = False)
            embed.add_field(name = 'Before:',value ='{}'.format(before.content),inline = False)
            embed.add_field(name = 'After:',value ='{}'.format(after.content),inline = False)
            embed.add_field(name = 'Channel:',value ='{}'.format(before.channel.name),inline = False)
            embed.timestamp = datetime.datetime.utcnow()
            await client.send_message(channel, embed=embed)

client.run('NTYzNjU5Nzg3NjA3MzQzMTM1.XKg2vQ.9T2sTj8yi12RFqxBUvpCQBnrH1k')
