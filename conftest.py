import pytest
import requests


class APIClient:

    def __init__(self, base_address):
        self.base_address = base_address


    def get(self, params=None):
        return requests.get(url=self.base_address, params=params)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.nasa.gov/planetary/apod?api_key=SafWqD3sCnzQZkfGJvDJa6htQsxC1aaoxCndnQix",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
