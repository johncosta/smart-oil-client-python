from urllib.parse import urljoin

import requests


class Client:
    SMARTOIL_API_URL="https://api.dropletfuel.com"
    TOKEN_PATH="/token.php"
    LATEST_PATH="/auto/get_tank_data.php"
    AJAX_DATA="/ajax/main_ajax.php"

    def __init__(self, client_id=None, client_secret=None):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token = self._get_token(self._client_id, self._client_secret)

    @staticmethod
    def _get_token(client_id, client_secret) -> str:
        """Retrieves a bearer token used for api calls """
        url = urljoin(Client.SMARTOIL_API_URL, Client.TOKEN_PATH)
        response = requests.post(url, data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        })
        response.raise_for_status()
        return response.json()["access_token"]

    def _get_latest_tank_data(self) -> dict:
        """Retrieves the latest tank data for all configured tanks"""
        url = urljoin(Client.SMARTOIL_API_URL, Client.LATEST_PATH)
        response = requests.get(url, headers={
                'Authorization': f'Bearer {self._token}'
            })
        response.raise_for_status()
        return response.json()
