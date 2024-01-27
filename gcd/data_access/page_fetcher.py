import requests
from typing import cast

class PageFetcher:
    @staticmethod
    def fetch(url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return cast(str, response.content.decode("utf-8"))
