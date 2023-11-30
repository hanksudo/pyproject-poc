import requests
from pydantic import BaseModel
from requests import Response


class Test(BaseModel):
    name: str


if __name__ == "__main__":
    response: Response = requests.get("https://github.com")
    print(response.text)
