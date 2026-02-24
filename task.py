# from rq import Queue
# from redis import Redis
# import logging

# import time

# # q = Queue(connection=Redis())

# # logging.warning("XS")


# # def count():
# #     logging.warning("Started")
# #     time.sleep(5)
# #     logging.warning("Done")


# # q.enqueue(count)


# # from pysolana.api import *
# # from pysolana.sol import *


# # print(getTransactionCount())  # 555309062
# # largest_accounts = getParsedTokenAccountsByOwner(
# #     PublicKey("5WZPN18c6QGrU1rGW7n6AXWFEFkz2urwZ162n5HjrUxt"),
# #     {"encoding": "base58"},
# #     None,
# # )["result"]["value"]

# # # Replace with the XCoin token address
# # TOKEN_ADDRESS = "XCoinTokenAddressHere"

# # # Connect to the Solana cluster (using devnet as an example)
# # client = RPCClient("https://api.devnet.solana.com")


# # def get_top_token_holders(token_address):
# #     # Get the largest accounts for a given mint
# #     largest_accounts = client.get_token_accounts_by_owner(
# #         PublicKey(token_address), {"encoding": "base58"}, None
# #     )["result"]["value"]

# #     parsed_accounts = [
# #         {
# #             "address": account["pubkey"],
# #             "amount": str(account["account"]["data"]["parsed"]["info"]["tokenAmount"]),
# #         }
# #         for account in largest_accounts[:10]
# #     ]

# #     print("Top Token Holders:\n")
# #     for idx, account in enumerate(parsed_accounts):
# #         print(f"{idx + 1}. Address: {account['address']}, Amount: {account['amount']}")


# # get_top_token_holders("5WZPN18c6QGrU1rGW7n6AXWFEFkz2urwZ162n5HjrUxt")

# import requests
# from bs4 import BeautifulSoup
# import re

# cookies = {
#     "chakra-ui-color-mode": "dark",
#     "_ga": "GA1.1.652773255.1712139288",
#     "cf_clearance": "dAjjtPukRpqY_Xj7grdczfY.CyPqOjA4zBkADdZ.8fY-1712368372-1.0.1.1-t7HpuPpAxeKoFHW22FG4o3oTDkj9NrwtiySmlTkhMs_wFYD.XJNV9ZH_pASgMwmbLBG8So333dqlVoj7xHdH3w",
#     "_ga_RD6VMQDXZ6": "GS1.1.1712368435.5.1.1712368526.0.0.0",
#     "__cf_bm": "7R5HE9hTzLAusV2cki_CorNQs_FS3HS76yNPcNKNZWE-1712372614-1.0.1.1-maAVzmKG3sGy047TtiHo2o7kHN5un0vpnwcuTDIiOTIlo8eDyhjJIE6Xsm5VofD_V_PLsf27xEUspwHYNzD9gwh.3xKzN.jZEkxOQcXQ8Ow",
#     "_ga_532KFVB4WT": "GS1.1.1712373930.19.0.1712373932.58.0.0",
# }

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "cache-control": "max-age=0",
#     # 'cookie': 'chakra-ui-color-mode=dark; _ga=GA1.1.652773255.1712139288; cf_clearance=dAjjtPukRpqY_Xj7grdczfY.CyPqOjA4zBkADdZ.8fY-1712368372-1.0.1.1-t7HpuPpAxeKoFHW22FG4o3oTDkj9NrwtiySmlTkhMs_wFYD.XJNV9ZH_pASgMwmbLBG8So333dqlVoj7xHdH3w; _ga_RD6VMQDXZ6=GS1.1.1712368435.5.1.1712368526.0.0.0; __cf_bm=7R5HE9hTzLAusV2cki_CorNQs_FS3HS76yNPcNKNZWE-1712372614-1.0.1.1-maAVzmKG3sGy047TtiHo2o7kHN5un0vpnwcuTDIiOTIlo8eDyhjJIE6Xsm5VofD_V_PLsf27xEUspwHYNzD9gwh.3xKzN.jZEkxOQcXQ8Ow; _ga_532KFVB4WT=GS1.1.1712373930.19.0.1712373932.58.0.0',
#     "referer": "https://dexscreener.com/solana/5WZPN18c6QGrU1rGW7n6AXWFEFkz2urwZ162n5HjrUxt?__cf_chl_tk=6Rew52RlKLmSssdyAgFx0ot2OnwNw8TAkoH_.w4nfEg-1712368359-0.0.1.1-1706",
#     "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
#     "sec-ch-ua-arch": '"x86"',
#     "sec-ch-ua-bitness": '"64"',
#     "sec-ch-ua-full-version": '"123.0.6312.105"',
#     "sec-ch-ua-full-version-list": '"Google Chrome";v="123.0.6312.105", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.105"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-model": '""',
#     "sec-ch-ua-platform": '"macOS"',
#     "sec-ch-ua-platform-version": '"14.3.0"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
# }

# html = requests.get(
#     "https://dexscreener.com/solana/bhvtfxmvgex9prqgsr6xr6bnzwubafedbsx6rprz9fgo",
#     headers=headers,
#     cookies=cookies,
# ).content


# soup = BeautifulSoup(html, "html.parser")

# element = soup.find(class_="custom-dx232q")

# url_to_match = r"https:\/\/dd\.dexscreener\.com\/ds\-data\/tokens\/[^\"\'\)]+"
# style_tag = soup.findAll("style")  # find the first style block

# for rule in style_tag[5].stripped_strings:
#     match = re.search(url_to_match, rule)
#     if match:
#         url = match.group(0).replace(")", "")
#         print(url)


b = ["dog", "cat", "hourse"]
c = b

print(c)

c.remove("cat")
print(b)
