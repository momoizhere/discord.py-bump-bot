import discord
from datetime import datetime
import time

token = ""

client = commands.Bot("$", self_bot=True)


# this is the on_ready event. this will run when the self bot starts up.
@client.event
async def on_connect():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel()
    
    while True:
        time.sleep(7200)
        await channel.send('!d bump')

    
    





client.run(token, bot=False)
