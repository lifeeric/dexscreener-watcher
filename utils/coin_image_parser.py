import requests
from bs4 import BeautifulSoup
import re
from utils.log import Logger


logger = Logger.init("Download_IMGE")


cookies = {
    "chakra-ui-color-mode": "dark",
    "_ga": "GA1.1.652773255.1712139288",
    "_ga_RD6VMQDXZ6": "GS1.1.1712368435.5.1.1712368526.0.0.0",
    "cf_clearance": "kyz4OO57PXH9UapXnNew51nINaqf_T7MM42DNJIDLLI-1712577181-1.0.1.1-HjRwwZZJtqJq1vG5wdpPkEY.jGUUVidCV_wfZvs4fypNm8zTvmvuQDSxYPBrDSDM9i7t3bNWVk3uqKmul7IfcA",
    "_ga_532KFVB4WT": "GS1.1.1712577158.26.1.1712577696.57.0.0",
    "__cf_bm": "gL68tSs_RvGon0Ekute.mJXlbrxDeJkY2qDu3JSJEwk-1712577983-1.0.1.1-9ulVaP0T8WVvEqZ5y8cMw9Wv7cS5UMu.TmlUWd42bnLAg8kDUIAQrmynEIwbYcHa_PxdMVdsezD.2qrYcD25xvbBMrRkmo0A5lcBhONa_lg",
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'chakra-ui-color-mode=dark; _ga=GA1.1.652773255.1712139288; _ga_RD6VMQDXZ6=GS1.1.1712368435.5.1.1712368526.0.0.0; cf_clearance=kyz4OO57PXH9UapXnNew51nINaqf_T7MM42DNJIDLLI-1712577181-1.0.1.1-HjRwwZZJtqJq1vG5wdpPkEY.jGUUVidCV_wfZvs4fypNm8zTvmvuQDSxYPBrDSDM9i7t3bNWVk3uqKmul7IfcA; _ga_532KFVB4WT=GS1.1.1712577158.26.1.1712577696.57.0.0; __cf_bm=gL68tSs_RvGon0Ekute.mJXlbrxDeJkY2qDu3JSJEwk-1712577983-1.0.1.1-9ulVaP0T8WVvEqZ5y8cMw9Wv7cS5UMu.TmlUWd42bnLAg8kDUIAQrmynEIwbYcHa_PxdMVdsezD.2qrYcD25xvbBMrRkmo0A5lcBhONa_lg',
    "origin": "https://dexscreener.com",
    "referer": "https://dexscreener.com/?__cf_chl_tk=aTf6fqrME51aOX16pMU9V0lbFqhdbK7Pu299wR_fddA-1712577998-0.0.1.1-1578",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"123.0.6312.107"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="123.0.6312.107", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.107"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"macOS"',
    "sec-ch-ua-platform-version": '"14.3.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}


def get_image(chain: str, ca: str) -> str:
    """
    Get the coin Image URL

    Args:
        chain: blockcain name
        ca: coin pair address

    Returns: image url
    """
    try:
        r = requests.get(
            f"https://dexscreener.com/{chain}/{ca}",
            headers=headers,
            cookies=cookies,
        )
        html = r.content

        soup = BeautifulSoup(html, "html.parser")

        url_to_match = r"https:\/\/dd\.dexscreener\.com\/ds\-data\/tokens\/[^\"\'\)]+"
        style_tag = soup.findAll("style")

        for rule in style_tag[5].stripped_strings:
            match = re.search(url_to_match, rule)

            if match:
                url = match.group(0).replace(")", "")
                return url
    except Exception as e:
        logger.error(f"get_image {e}")


if __name__ == "__main__":
    print(get_image("bhvtfxmvgex9prqgsr6xr6bnzwubafedbsx6rprz9fgo"))
