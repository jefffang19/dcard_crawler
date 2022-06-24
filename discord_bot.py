
# https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8

#導入 Discord.py
import discord
import crawler
import pandas as pd
import random

# read key token
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')
    
    elif message.content == '給我爬':
        crawler.crawl()
        await message.channel.send('開始爬了')
        
    elif message.content == '講笑話':
        df = pd.read_csv('list.csv')
        
        pick_idx = random.randint(1, len(df)-1)
        
        _url = df.iloc[pick_idx]['url']
        
        await message.channel.send(_url)

client.run(config['token']) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面