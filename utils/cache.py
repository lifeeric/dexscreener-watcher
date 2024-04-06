import redis
import json


class Cache:
    """Cache Class"""

    def __init__(self) -> None:
        self.client = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def save_coin(self, ca: str, id: int):
        """
        Store the essential info about coin pair

        Args:
            ca: coin pair address
            id: telegram message id
        """

        print(id)
        self.client.set(
            ca,
            json.dumps({"id": id}),
        )

    def check_coin(self, ca: str) -> bool:
        """
        Check if a coin has been previously saved.

        Args:
            ca: coin pair address

        Returns: boolean if exists True, else False
        """

        r = self.client.get(ca)

        if r:
            return json.loads(r)
        else:
            False
