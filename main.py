import discord
from discord.ext import commands
from random import randint
import youtube_dl
import os

client = commands.Bot(command_prefix='!')


@commands.command()
async def d(ctx, arg1):
    arg1 = int(arg1)
    arg1 = randint(1, arg1)
    await ctx.send(arg1)


client.add_command(d)


@commands.command()
async def toque(ctx, url: str, channel):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()

client.add_command(toque)


@commands.command()
async def saia(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected:
        await voice.disconnect()
    else:
        await ctx.send('O bot não está conectado à esta call')


client.add_command(saia)


@commands.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('O bot não está reproduzindo nenhum audio')


client.add_command(pause)


@commands.command()
async def continuar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('O audio já está sendo reproduzido')


client.add_command(continuar)


@commands.command()
async def pare(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.add_command(pare)

client.run('OTEwMjk4NTE3OTQyMTkwMTUx.YZQzjw.Hvuk78cntpDzU6JQj1mG8gRXqHw')
