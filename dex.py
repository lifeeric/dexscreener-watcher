import json
import httpx
import time
from typing import List
import asyncio
from websockets import connect
from pprint import pprint
from datetime import date
from rq import Retry


from utils.log import Logger
from utils.cache import Cache
from utils.worker import q
from utils.job_message import save_and_send_notification

logger = Logger().init("DexScreener")


# Blockchain: Base & Solana
# Condition:
# Liquidity > $1000
# List 1 hour ago
# in last 5min, 3+ buy

# logging.basicConfig(level=logging.INFO)


# async def coin_info() -> None:
#     with httpx.Client() as client:
#         r = await client.get("https://api.dexscreener.com/latest/dex/pairs/")
#         pprint(r)

# async def fetch_sol_coins() -> None:
#     ws_url = "wss://io.dexscreener.com/dex/screener/pairs/h24/1?rankBy[key]=volume&rankBy[order]=desc&filters[liquidity][min]=1000&filters[marketCap][min]=30000&filters[pairAge][min]=1&filters[pairAge][max]=24&filters[buys][m5][min]=3&filters[chainIds][0]=solana"

#     try:
#         with open("./header.json", "r") as f:
#             headers = json.loads(f.read())
#             del headers["Origin"]
#             del headers["Host"]

#         async with open_websocket_url(
#             ws_url,
#             extra_headers=headers,
#         ) as ws:
#             r = await ws.get_message()
#             print(r)

#     except Exception as e:
#         logging.error("[❌]", e)

# async def main() -> None:

# try:
#     with open("./header.json", "r") as f:
#         headers = json.loads(f.read())
#         del headers["Origin"]
#         del headers["Host"]
#         headers = [(k, v) for k, v in headers.items()]
#         print(headers)

#     async with open_websocket_url(
#         ws_url,
#         extra_headers=headers,
#     ) as ws:
#         r = await ws.get_message()
#         logger.info(r)
# except Exception as e:
#     logger.error("[❌]", e)

# async with trio.open_nursery() as nursery:
#     nursery.start_soon(fetch_sol_coins)


class DexScreener:

    def __init__(self, url) -> None:
        self.url = url
        self.loop = asyncio.new_event_loop()
        self.cache = Cache()

        with open("./headers.json") as f:
            self.headers = json.load(f)

    def watcher(self):
        return self.loop.run_until_complete(self._sol_coins())

    async def _sol_coins(self):

        try:

            async with connect(self.url, extra_headers=self.headers) as ws:
                while True:
                    coins = json.loads(await ws.recv())
                    try:
                        if type(coins) == dict and coins.get("type", {}) == "pairs":
                            await self._create_job_for_coin(coins)

                            logger.info("[⏱] listening...")
                            await asyncio.sleep(10)
                    except Exception as e:
                        logger.info(f"[⚠️] {e}")
                        pass

        except Exception as e:
            logger.error(f"[❌] {e}")

    async def _create_job_for_coin(self, coins: List) -> None:
        """Parse coin pair address and create job"""

        for coin in coins.get("pairs", {}):

            coin_details = {
                "name": coin.get("baseToken").get("name", ""),
                "symbol": coin.get("baseToken").get("symbol", ""),
                "ca": coin.get("pairAddress", ""),
                "priceUsd": coin.get("priceUsd", 0),
                "marketCap": coin.get("marketCap", 0),
                "liquidity": coin.get("liquidity", 0),
                "priceChange": coin.get("priceChange", 0),
                "pairCreatedAt": coin.get("pairCreatedAt", 0),
                "img": coin.get("profile", {}).get("imgKey", ""),
            }

            if not self.cache.check_coin(coin_details.get("ca")):
                q.enqueue(
                    save_and_send_notification,
                    args=(coin_details,),
                    retry=Retry(max=10),
                )

        with open("./docs/data.json", "w") as f:
            json.dump(coins, f)


if __name__ == "__main__":
    ws_url = "wss://io.dexscreener.com/dex/screener/pairs/h24/1?rankBy[key]=volume&rankBy[order]=desc&filters[liquidity][min]=1000&filters[marketCap][min]=30000&filters[pairAge][min]=1&filters[pairAge][max]=24&filters[buys][m5][min]=3&filters[chainIds][0]=solana"

    dex = DexScreener(ws_url)
    dex.watcher()
