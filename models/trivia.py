import requests


class Trivia:
    def __init__(self, key: str) -> None:
        self.url = "https://api.api-ninjas.com/v1/facts?limit=1"
        self.key = key

    def fetch(self) -> dict:
        response = requests.get(self.url, headers={"X-Api-Key": self.key})
        if response.status_code == requests.codes.ok:
            return {"status": 1, "msg": response.text}
        else:
            return {"status": 0, "msg": response.text}