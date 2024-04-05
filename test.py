from websockets import connect  # type: ignore
import asyncio
from pprint import pprint
import json
from redis import Redis
from rq import Queue
import time

# from task import count
from wr import q
import logging

# async def run():
#     # ws_url = "wss://io.dexscreener.com/dex/screener/pairs/h24/1?rankBy[key]=volume&rankBy[order]=desc&filters[chainIds][0]=solana&filters[pairAge][max]=24"
#     ws_url = "wss://io.dexscreener.com/dex/screener/pairs/h24/1?rankBy[key]=volume&rankBy[order]=desc&filters[liquidity][min]=1000&filters[marketCap][min]=30000&filters[pairAge][min]=1&filters[pairAge][max]=24&filters[buys][m5][min]=3&filters[chainIds][0]=solana"

#     with open("./header.json", "r") as f:
#         headers = f.read()

#     async with connect(ws_url, extra_headers=headers) as websocket:
#         while True:
#             message = await websocket.recv()
#             pprint(json.loads(message))

#             with open("./data.json", "a+") as f:
#                 json.dump(json.loads(message), f)


# if __name__ == "__main__":
#     # asyncio.run(run())

q = Queue(connection=Redis())


# def bar():
#     logging.warning("started")
#     time.sleep(4)
#     logging.warning("done")


# def foo():
#     r = q.enqueue(count)
#     print(r)


# if __name__ == "__main__":
# foo()

from telethon import TelegramClient, events  # type: ignore # ignore:
from telethon.tl.types import InputPeerUser, InputPeerChat, PeerChannel

# from telethon.tl.types import , PeerChat, PeerUser
from telethon.tl.custom import Button


# from telethon.tl.custom.button import Button

with open("./config.json", "r") as f:
    config = json.load(f)
    api_id = config.get("api_id")
    api_hash = config.get("api_hash")
    channel_id_test = config.get("channel_id_test")


# with TelegramClient("user", api_id, api_hash) as client:
#     msg = f"""
# **Cat/SOL**

# ## Hi
# 🚀 Price: $19.93 (0.1 SOL)
# 📊 Current Market Cap: $6,968
# 📈 Price Change: +50% in last 24 hours
# 📈 Supply: 1,140,868 ZAZACAT
# 🌐 Liquidity Pool: DEX Tools, SolScan

# Link: [ls](https://dexscreener.com/solana/) | [inline URL](https://www.example.com/)

# """
#     # button = Button.inline("Click Here", f"https://t.me/SolTradingBot?start")
#     #    client.send_message(chat, 'Welcome', )

#     r = client.send_message(
#         entity=channel_id_test,
#         message=msg,
#         buttons=[
#             Button.text("Thanks!", resize=True, single_use=True),
#             Button.request_phone("Send phone"),
#             Button.request_location("Send location"),
#         ],
#     )

#     # r = client.edit_message("https://t.me/+WIJV81tlhXllY2Nh", 399, msg)
#     print(r.id)

client = TelegramClient("bot", api_id, api_hash)


@client.on(events.CallbackQuery)
async def callback(event):
    await event.edit("Thank you for clicking {}!".format(event.data))


# client.send_message(
#     channel_id_test,
#     'A single button, with "clk1" as data',
#     buttons=Button.inline("Click me", b"clk1"),
# )


@client.on(events.NewMessage())
async def kucoin_event_handler(event):
    message = event.text
    # PeerChannel(channel_id=channel_id_test)
    print(await client.get_entity(channel_id_test))

    # print(f"🔺 Client {message}")

    # trio.run(watch, message)
    # await bot.send_message("eric_git", "Ordered!")

    await client.send_message(
        channel_id_test,
        "Pick one from this grid",
        buttons=[
            [Button.inline("Left"), Button.inline("Right")],
            [Button.url("Check this site!", "https://lonamiwebs.github.io")],
        ],
    )


client.start()

client.loop.run_forever()

# import pytz
# from datetime import datetime


# import time
# import math


# import datetime


# def time_since(timestamp):
#     now = datetime.datetime.now()
#     diff = now - datetime.datetime.fromtimestamp(timestamp / 1000.0)  # convert ms -> s

#     if diff.total_seconds() < 60:
#         return f"{diff.total_seconds()} seconds ago"
#     elif diff.total_seconds() < 3600:
#         minutes = int(diff.total_seconds() // 60)
#         seconds = int(diff.total_seconds() % 60)
#         return f"{minutes} minute{(minutes != 1 and 's')} and {seconds} second{'s' if seconds > 1 else ''} ago"
#     elif diff.total_seconds() < 86400:
#         hours = int(diff.total_seconds() // 3600)
#         minutes = int((diff.total_seconds() % 3600) // 60)
#         return f"{hours} hour{'s' if hours > 1 else ''} and {minutes} minute{'s' if minutes > 1 else ''} ago"
#     else:
#         days = int(diff.total_seconds() // 86400)
#         hours = int(((diff.total_seconds() % 86400) // 3600))
#         return f"{days} day{'s' if days > 1 else ''} and {hours} hour{'s' if hours > 1 else ''} ago"


# Example usage
# post_timestamp = 1712260802000
# print(type(1712260802000))
# print(time_since(post_timestamp))


# import pandas as pd


# # create a sample DataFrame with numerical values
# data = {"Value": [3000, 2000000, 3000000, 4000000]}
# df = pd.DataFrame(data)

# # format the values as currency in millions
# df["Value"] = df["Value"]
# df["Value"] = df["Value"].map("${:,.2f}M".format)


# def currency_format(value):
#     if value >= 1000000000:
#         return f"{value/1000000000:.2f}B"
#     elif value >= 1000000:
#         return f"{value/1000000:.2f}M"
#     elif value >= 1000:
#         return f"{value/1000:.2f}K"
#     else:
#         return f"{value:.0f}"


# print(currency_format(3800))
