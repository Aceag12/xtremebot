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

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Counting Latency...')
    await asyncio.sleep(3)
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 100
    await client.edit_message(t, new_content='Pong! Latency Took: `{}ms`'.format(int(ms)))
    await client.send_typing(ctx.message.channel)

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Discord Avatar Machine', description='**__Avatar of {0}:__**'.format(ctx.message.author), color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar Machine', description="**__Avatar of {0}:__**".format(user), color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)  

@client.command(pass_context=True)
async def servers(ctx):
    if ctx.message.author.id == '519122918773620747':
        servers = '\n'.join([i.name for i in client.servers]).strip('\n')
        await client.say('**I am currently on these servers:**\n ```bf\n{}```'.format(servers))
    else:
        await client.say('This command is for bot owner only.')        
      
@client.command(pass_context=True)
async def serverlist(ctx):
    if ctx.message.author.id == '460108004835065866':
        servers = '\n'.join([i.name for i in client.servers]).strip('\n')
        await client.say('**I am currently on these servers:**\n ```bf\n{}```'.format(servers))
    else:
        await client.say('This command is for bot owner only.')      
      
@client.command(pass_context=True)      
async def guildinfo(ctx):

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: 
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Server Owner__', value = str(server.owner) + "\n **__Owner's ID__**  " + server.owner.id);
    join.add_field(name = '__Server ID__', value = str(server.id))
    join.add_field(name = '__Members Count Of This Server__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels in this server__', value = str(channelz));
    join.add_field(name = '__Available Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='__Server was Created on__: %s'%time);

    return await client.say(embed = join);      
      
@client.command(pass_context=True)
async def pong(ctx):
    t = await client.say('Counting Latency...')
    await asyncio.sleep(3)
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 100
    await client.edit_message(t, new_content='Pong! Latency Took: `{}ms`'.format(int(ms)))
    await client.send_typing(ctx.message.channel)

@client.command(pass_context = True)
async def whois(ctx, user: discord.Member=None):
    if user is None:
      await client.say('Please tag a user to get user information. Example- ``ad!whois @user``')
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here is the detail of that user.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="__Name__", value=user.mention, inline=True)
      embed.add_field(name="__USER ID__", value=user.id, inline=True)
      embed.add_field(name="__Status__", value=user.status, inline=True)
      embed.add_field(name="__Highest role__", value=user.top_role)
      embed.add_field(name="__Color__", value=user.color)
      embed.add_field(name="__Playing__", value=user.game)
      embed.add_field(name="__Nickname__", value=user.nick)
      embed.add_field(name="__Joined__", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="__Created__", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed) 
      
@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def setnickname(ctx, user: discord.Member=None, *, nickname=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to change nickname. Example- `` ad!setnick @user <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      await client.say('Nickname was successfully changed.')

@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def resetnickname(ctx, user: discord.Member=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to reset nickname. Example- ``ad!resetnick @user``')
      return
    else:
      nick = user.name
      await client.change_nickname(user, nick)
      await client.delete_message(ctx.message)
      await client.say('Nickname reset was successful.')
      
@client.command(pass_context = True)
async def channellock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("{0} Just Locked {1}.".format(ctx.message.author, ctx.message.channel))
    else:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command.**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("{0} Just Locked {1}.".format(ctx.message.author, channelname))

@client.command(pass_context = True)
async def channelunlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("{0} Unlocked {1}.".format(ctx.message.author, ctx.message.channel))
    else:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("{0} Unlocked {1}".format(ctx.message.author, channelname))
            
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)
  for channel in ctx.message.author.server.channels:
        if channel.name == '〚📑〛extreme-logs':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Bulk Message Deleted')
            embed.add_field(name = '__Commander:__ **{0}**'.format(ctx.message.author),value ='__Commander ID:__ **{}**'.format(ctx.message.author.id),inline = False)
            embed.add_field(name = '__Channel:__',value ='{}'.format(ctx.message.channel),inline = False)
            await client.send_message(channel, embed=embed)
            await client.say('Purged **{}** Messages For You'.format(number))
            
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
        return
    else:    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='HELP CENTER OF EXTREMEMODERATOR BOT')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name = '__**LOGGING:**__',value ='`e.setlogs`',inline = False)
        embed.add_field(name = '__**AVATAR:**__',value ='`e.avatar`',inline = False)
        embed.set_footer(text ='CREATED BY ALISTORM||ASH KETCHUM')
        await client.say(embed=embed)
        
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = '〚📑〛extreme-logs'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in message.author.server.channels:
        if channel.name == '〚📑〛extreme-logs':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(logchannel,  embed=embed)
          
          
@client.event
async def on_reaction_add(reaction, user: discord.Member=None):
  for channel in user.server.channels:
    if channel.name == '〚📑〛extreme-logs':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Added')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)
        
@client.event
async def on_reaction_remove(reaction, user: discord.Member=None):
  for channel in user.server.channels:
    if channel.name == '〚📑〛extreme-logs':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Removed')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)        
        
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

@client.command(pass_context=True)
async def invite(ctx):
    if ctx.message.author.bot:
        return
    else: 
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = '__**INVITE LINK:**__',value ='https://discordapp.com/oauth2/authorize?client_id=563659787607343135&scope=bot&permissions=2146958591',inline = False)  
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def botinfo(ctx):
    if ctx.message.author.bot:
        return
    else: 
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = '__**BOT INFO:**__',value ='This is a bot created by  Ash Ketchum#4757 and ALISTORM#2930 together. They worked Hard and made me. I am made through python and have cool command so test them all.',inline = False)  
        embed.add_field(name = '__**JOIN OUR OFFICIAL GUILD:**__',value ='https://discord.gg/XB3zwXs',inline = False)  
        await client.say(embed=embed)        
            
client.run('NTYzNjU5Nzg3NjA3MzQzMTM1.XKg2vQ.9T2sTj8yi12RFqxBUvpCQBnrH1k')
