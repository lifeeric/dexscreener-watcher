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
    channel = config.get("channel_id")
    test_channel = config.get("channel_id_test")
    IS_DEV = config.get("is_dev")


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
        chain,
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

    trx = (
        f"[SOLSCAN](https://solscan.io/account/{ca})"
        if chain == "solana"
        else f"[BaseScan](https://basescan.org/address/{ca})"
    )

    msg = f"""
{ca}

**`{symbol} — {name}`**


🚀 Launch: {time_since(pairCreatedAt)}
⬆️ Price: **${priceUsd}**
💰 Market Cap: **${currency_format(marketCap)}**
📈 Price Change: **{priceChange.get('h1')}%** in last 1 hour
💧 Liquidity: **${currency_format(liquidity.get('usd'))}**

[DEXScreener](https://dexscreener.com/{chain}/{ca}) │ {trx}
    """

    return msg


def save_and_send_notification(coin) -> None:
    """"""
    logger.info("[📣] Sending...")

    with TelegramClient("user", api_id, api_hash) as client:
        id = test_channel if IS_DEV else channel

        msg = format_msg(coin)

        if img := coin.get("img"):
            pass
            r = client.send_file(id, file=img, caption=msg)
        else:
            r = client.send_message(id, message=msg)
            pass

        cache = Cache()
        cache.save_coin(coin.get("ca"), id=r.id)
        logger.info("[✅📣] Sent & Saved")
    # time.sleep(60)
