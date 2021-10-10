from datetime import datetime
import configparser
import discord
import time

start = 0

config = configparser.ConfigParser()
config.read('../../discordtoken.ini')
token = config['discord']['token']
client = discord.Client()


@client.event
async def on_ready():
    print('Bot online')

async def timer():
    channel = client.get_channel(id=785889829522243617)
    
    config_status_all = "09:55:00"
    #config_system_all = 
    #config_uptime_all = 
    #config_kernel_all = 

    date = datetime.now()
    current_time = date.strftime("%H:%M:%S")
    ctime = str(current_time)

    if ctime == config_status_all:
        await channel.send("test")
        print ("Test")
        time.sleep(2)

client.loop.create_task(timer())
client.run(token)