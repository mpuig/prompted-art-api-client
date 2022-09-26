import json
from urllib.request import Request, urlopen


class PromptedAPIError(Exception):
    """An exception class for the client"""


class PromptedAPI:
    url_path = "/api/v1"

    def __init__(self, api_key: str, url: str = "https://prompted.art"):
        self.api_key = api_key
        self.url = url

    def create_prompt(self, data=None):
        if data is None:
            data = {}

        url = f"{self.url}{self.url_path}/prompts/"
        headers = {
            "Authorization": f"Token {self.api_key}",
            "Content-Type": "application/json",
        }

        request = Request(
            url=url,
            data=json.dumps(data).encode("ascii"),
            headers=headers,
            method="POST",
        )
        with urlopen(request) as response:
            response_status_code = response.status
            response_data = json.load(response)

        if response_status_code != 201:
            reason = self.parse_reason(response.headers)
            raise PromptedAPIError(
                f"Wrong request, status code is {response_status_code}, reason is {reason}"
            )

        if not response_data:
            raise PromptedAPIError("Wrong request, content response is empty")

        return response_data

    @staticmethod
    def parse_reason(headers):
        if "X-Status-Reason" not in headers:
            return "Unknown Error"
        return headers["X-Status-Reason"]

