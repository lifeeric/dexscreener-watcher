import time
import json
from telethon import TelegramClient, sync
from typing import Dict

from utils.log import Logger
from utils.cache import Cache
from utils.time_converter import time_since


logger = Logger.init("TG")


with open("./config.json", "r") as f:
    config = json.load(f)
    api_id = config.get("api_id")
    api_hash = config.get("api_hash")


def currency_format(value: str) -> str:
    """
    Convert number into M, K, B

    Args:
        value: numbers

    Example: 2K, 1.2M
    """
    if value >= 1000000000:
        return f"{value/1000000000:.2f}B"
    elif value >= 1000000:
        return f"{value/1000000:.2f}M"
    elif value >= 1000:
        return f"{value/1000:.2f}K"
    else:
        return f"{value:.0f}"


def format_msg(coin: Dict) -> str:
    (
        name,
        symbol,
        ca,
        priceUsd,
        marketCap,
        liquidity,
        priceChange,
        pairCreatedAt,
        img,
    ) = [coin[k] for k in coin]

    msg = f"""
{ca}

**`{symbol} — {name}`**


🚀 Launch: {time_since(pairCreatedAt)}
⬆️ Price: **${priceUsd}**
💰 Market Cap: **${currency_format(marketCap)}**
📈 Price Change: **{priceChange.get('h1')}%** in last 1 hour
💧 Liquidity: **${currency_format(liquidity.get('usd'))}**

[DEXScreener](https://dexscreener.com/solana/{ca}) │ [SOLSCAN](https://solscan.io/account/{ca})
    """

    return msg


def save_and_send_notification(coin) -> None:
    """"""
    time.sleep(60)
    logger.info("[📣] Sending...")

    with TelegramClient("user", api_id, api_hash) as client:
        msg = format_msg(coin)
        r = client.send_message(entity="https://t.me/+WIJV81tlhXllY2Nh", message=msg)

        cache = Cache()
        cache.save_coin(coin.get("ca"), id=r.id)
        logger.info("[✅📣] Sent & Saved")
