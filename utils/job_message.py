import time
import json
from datetime import date
from telethon import TelegramClient, sync

from utils.log import Logger
from utils.cache import Cache


logger = Logger.init("TG")


with open("./config.json", "r") as f:
    config = json.load(f)
    api_id = config.get("api_id")
    api_hash = config.get("api_hash")


# class MessageSender:
#     """Interact with telegram class"""

#     def __init__(self):
#         with open("./config.json", "r") as f:
#             self.config = json.load(f)
#             self.api_id = self.config.get("api_id")
#             self.api_hash = self.config.get("api_hash")
#             print(self.config)

#         self.bot = TelegramClient("user", self.api_id, self.api_hash)

#     async def connect(self):
#         """Start the bot with token"""
#         await self.bot.start()

#     async def send_message(self, text: str = "") -> None:
#         """
#         Broadcast Coin to channel

#         Args:
#             text: coin details
#         """

#         try:
#             await self.bot.send_message(
#                 entity="https://t.me/+WIJV81tlhXllY2Nh", message="text"
#             )
#             logger.info(f"Successfully broadcasted")

#         except Exception as e:
#             logger.error(f"[❌] {e}")

#     async def disconnect(self):
#         await self.bot.disconnect()


def save_and_send_notification(
    address, pair, priceUsd, marketCap, liquidity, priceChange
) -> None:
    """"""

    logger.info("[📣] Sending...")

    with TelegramClient("user", api_id, api_hash) as client:
        msg = f"""
**{pair}**

🚀 Price: ${priceUsd} (0.1 SOL)
📊 Current Market Cap: ${marketCap}
📈 Price Change: {priceChange.get('h24')}% in last 24 hours
🌐 Liquidity: ${liquidity.get('usd')}

[DEX](https://dexscreener.com/solana/{address})

    """
        client.send_message(entity="https://t.me/+WIJV81tlhXllY2Nh", message=msg)

    cache = Cache()
    today = date.today()
    cache.save_coin(address, notficationSent=True, date=today)
    logger.info("[✅📣] Sent & Saved")
