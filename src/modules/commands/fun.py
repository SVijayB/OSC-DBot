from urllib.request import urlopen
from datetime import datetime
import discord
import random
import json


class fun:
    def jokes(data):
        try:
            arg = data[1]
        except:
            arg = ""
        url = "https://v2.jokeapi.dev/joke/Any"
        link_url_arg = {
            "misc": "https://v2.jokeapi.dev/joke/Misc",
            "coding": "https://v2.jokeapi.dev/joke/Programming",
            "dark": "https://v2.jokeapi.dev/joke/Dark",
            "pun": "https://v2.jokeapi.dev/joke/Pun",
            "spooky": "https://v2.jokeapi.dev/joke/Spooky",
        }
        if arg in link_url_arg:
            url = link_url_arg[arg]
        response = urlopen(url)
        joke_data = json.loads(response.read())
        if joke_data["type"] == "single":
            embed = discord.Embed(
                title="😜  Jokes | " + joke_data["category"],
                description=joke_data["joke"],
                color=discord.Color.from_rgb(47, 49, 54),
                timestamp=datetime.utcnow(),
            )
        if joke_data["type"] == "twopart":
            embed = discord.Embed(
                title="😜  Jokes | " + joke_data["category"],
                color=discord.Color.from_rgb(47, 49, 54),
                timestamp=datetime.utcnow(),
            )
            embed.add_field(
                name=joke_data["setup"], value=joke_data["delivery"], inline=False
            )
        return embed

    def quotes():
        response = urlopen("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        data = json.loads(response.read())
        data = data["data"][0]

        embed = discord.Embed(
            title="✌️  Quotes",
            description=data["quoteText"],
            color=discord.Color.from_rgb(47, 49, 54),
        )
        embed.set_footer(text="Quote by " + data["quoteAuthor"])
        return embed

    def memes():
        urls = [
            "https://meme-api.herokuapp.com/gimme/",
            "https://meme-api.herokuapp.com/gimme/ProgrammerHumor",
        ]
        response = urlopen(random.choice(urls))
        data = json.loads(response.read())

        embed = discord.Embed(
            title="😾  Memes",
            url=data["postLink"],
            description="Subreddit | " + data["subreddit"],
            color=discord.Color.from_rgb(47, 49, 54),
        )
        embed.set_image(url=data["preview"][-1])
        return embed
