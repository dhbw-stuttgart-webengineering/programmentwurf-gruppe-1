"""Dualis Session Class"""

import logging
import re
import bs4
import requests
from .exceptions import NoUsernameorPasswordException, InvalidUsernameorPasswordException

logger = logging.getLogger(__name__)


class DualisSession(requests.Session):
    """Dualis session class

    Args:
        requests (_type_): Session Class
    """

    def __init__(self, username: str, password: str):
        """Constructor

        Args:
            username (str): username as E-Mail
            password (str): Password

        Raises:
            Exception: If no username or password is provided
        """
        super().__init__()

        if password is None or username is None:
            raise NoUsernameorPasswordException(
                "No username or password provided")

        self._payload = {
            'usrname': username,
            'pass': password,
            'APPNAME': 'CampusNet',
            'PRGNAME': 'LOGINCHECK',
            'ARGUMENTS':
                'clino,usrname,pass,menuno,menu_type,browser,platform',
            'clino': '000000000000001',
            'menuno': '000324',
            'menu_type': 'classic',
            'browser': '',
            'platform': ''
        }

        self._header = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/86.0.4240.111 Safari/537.36',
                        'origin': 'https://dualis.dhbw.de',
                        'referer': 'https://dualis.dhbw.de/'
                        }

        self._auth_token = self._create_authtoken()

    def get(self, url, **kwargs) -> bs4.BeautifulSoup:
        response = super().get(url, **kwargs)
        response.encoding = 'UTF-8'
        return bs4.BeautifulSoup(response.text, "html.parser")

    def _create_authtoken(self):
        """Creates the authToken

        Returns:
            authToken (str): authToken
        """

        post_url = "https://dualis.dhbw.de/scripts/mgrqispi.dll"
        response = self.post(post_url,
                             data=self._payload,
                             verify=False)
        try:
            url_index = response.headers["REFRESH"].index("URL=") + len("URL=")
        except Exception as e:
            raise InvalidUsernameorPasswordException from e
        redirect_url = "https://dualis.dhbw-stuttgart.de" + \
            response.headers["REFRESH"][url_index:]
        session_id = re.search('ARGUMENTS=-N([0-9]{15})', redirect_url)

        return session_id.group()[-15:]

    def get_authtoken(self):
        """Returns the authToken

        Returns:
            str: authToken
        """
        return self._auth_token
