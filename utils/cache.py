import redis


class Cache:
    """Cache Class"""

    def __init__(self) -> None:
        self.client = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def save_coin(self, address: str, notficationSent: bool, date: str):
        """
        Store the essential info about coin pair

        Args:
            address: coin pair address
            notficationSent: if notified tg True, else False
            date: last update date
        """
        self.client.hmset(
            address,
            {"notficationSent": notficationSent, "updated": date},
        )

    def check_coin(self, address: str):
        """
        Check if a coin has been previously saved.

        Args:
            address: coin pair address

        Returns: boolean if exists True, else False
        """

        r = self.client.get(address)

        if r:
            return True
        else:
            False
