import discord
import asyncio
import json
import sys
from datetime import datetime
import requests
import random
from itertools import cycle
from discord.ext import commands, tasks
import time

token = "NzgzMzY3MjQ4NTU5MDc5NDU0.X8bL4Q.qvsvWFWD_mzRYF2oL9aLXCM1Q3o"

client = commands.Bot("$", self_bot=True)


# this is the on_ready event. this will run when the self bot starts up.
@client.event
async def on_connect():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel(783470458426359858)
    
    while True:
        time.sleep(7200)
        await channel.send('!d bump')

    
    





client.run(token, bot=False)
