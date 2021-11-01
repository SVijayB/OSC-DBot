from urllib.request import urlopen
from dotenv import load_dotenv
from discord.ext import tasks, commands
import discord
import json
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='>')

@tasks.loop(seconds=10)
async def oscEventNotif():
    url = os.getenv('API')
    response = urlopen(url)

    event_data = json.loads(response.read())

    with open ('data.json', 'r') as f:
        local_data = json.load(f)
    if(local_data['eventID'] == event_data[-1]['_id']):
        print("No new events")
    else:
        local_data['eventID'] = event_data[-1]['_id']
        with open('data.json', 'w') as f:
            json.dump(local_data, f, indent=4, separators=(',', ': '))
        
        event = event_data[-1]

        message_channel = bot.get_channel(904455110212591676)
        embed=discord.Embed(title="Title", url="https://google.com/", description="Desc", color=0xFF5733)
        await message_channel.send(embed=embed)
        print("Notif sent")

oscEventNotif.start()
bot.run(TOKEN)