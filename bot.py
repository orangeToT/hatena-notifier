import os
import datetime
import json
from dotenv import load_dotenv
import discord
from discord.ext import tasks
import feedparser


load_dotenv()

rss_url = os.getenv("RSS_URL")
channel_list = os.getenv("CHANNEL_LIST").split(",")
token = os.getenv("TOKEN")

jst = datetime.timezone(datetime.timedelta(hours=9))

times = [ datetime.time(hour=x, tzinfo=jst) for x in range(24) ]

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):


    async def setup_hook(self):
        self.send_feed.start()

    @tasks.loop(time=times)
    async def send_feed(self):
        rss = feedparser.parse(rss_url)
        latest_id = rss.entries[0].id
        with open("last_id.json", "r") as f:
            last_id = json.load(f).get("last_id")

        
        if  last_id is None or latest_id != last_id:
            with open("last_id.json", "w") as f:
                json.dump({"last_id": latest_id}, f)

            for channel_id in channel_list:
                channel = await self.fetch_channel((channel_id))
                await channel.send("ブログに新しい記事が投稿されました！" + "\n\n" + rss["entries"][0]["title"] + "\n" + rss["entries"][0]["link"])
            print("New Paper was published!")
        else:
            print("No new paper!")

    @send_feed.before_loop
    async def before_send_feed(self):
        await self.send_feed()


client = MyClient(intents=intents)

client.run(token)
