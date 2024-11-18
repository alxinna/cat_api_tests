import os
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Union, Dict, List


@dataclass
class TestArgsApi:
    api_key: str = None
    base_url: str = "https://api.thecatapi.com/v1"
    default_headers = {
        'Content-type': 'application/json'
    }

    def __post_init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')


@dataclass
class ApiResponse:
    status_code: int
    body: Union[None, str]
    json: Union[None, Dict, List]
