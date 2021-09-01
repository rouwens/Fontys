
import discord
import os
import configparser
from discord import message
from discord.ext import commands
import sys
import ipaddress

bot = commands.Bot(command_prefix='.')

#Importeren van de Discord token.
config = configparser.ConfigParser()
config.read('/home/daan/Bureaublad/School/Github/discordtoken.ini')
token = config['discord']['token']
channelid = config['discord']['channelid']
channel = bot.get_channel(channelid)



def sysmanagement(arg):
    host = arg
    ip = ipaddress.ip_address(host)
    
    @bot.command()
    async def re(ctx):
        return()
    
    @bot.command()
    async def exit(ctx):
        await ctx.send("Bot is shutting down :(")
        sys.exit()
    
    
    #Reset host
    @bot.command()
    async def reset_host(ctx):
        os.startfile(sys.argv[0])
        sys.exit()
    
    # Kernel commands
    @bot.command()
    async def kernel(ctx, arg):
        if arg == 'run':
            cmd = "ssh {0} -l root 'uname -r'".format(ip)
            exec = os.popen(cmd).read()
            await ctx.send(exec)
        
        else:
            print ()
        
    @bot.command()
    async def date(ctx, arg):
        if arg == 'full':
            cmd = "ssh {0} -l root 'date'".format(ip)
            exec = os.popen(cmd).read()
            await ctx.send(exec)
        
        if arg == 'time':
            cmd = "ssh {0} -l root 'date +'%T''".format(ip)
            exec = os.popen(cmd).read()
            await ctx.send(exec)
        


@bot.event
async def on_ready():
    print('Bot online')
    await channel.send('hello')

#Afsluiten van de bot
#@bot.command()
#async def exit(ctx):
#    await ctx.send("Bot is shutting down :(")
#    sys.exit()


@bot.command()
async def set_host(ctx, arg):
    mes = "Host is set on " + arg
    await ctx.send(mes)
    sysmanagement(arg)

bot.run(token)

