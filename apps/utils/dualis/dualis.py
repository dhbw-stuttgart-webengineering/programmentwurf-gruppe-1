"""Dualis class"""

import logging

from .dualis_session import DualisSession
from .webscraper import WebScraper

logger = logging.getLogger(__name__)


class Dualis:
    """Dualis class
    """

    def __init__(self, username: str, password: str):
        """Constructor

        Args:
            username (str): Username as E-Mail
            password (str): Password
        """

        self.session = DualisSession(username, password)
        self.webscraper = WebScraper(session=self.session)

    def get_name(self) -> str:
        """Returns the name of the user

        Returns:
            str: Name of the user
        """
        return self.webscraper.scrape_username()

    def get_grades(self) -> list:
        """Return a List of Module Objects that contain all Units

        Returns:
            list: List of Module Objects
        """
        return self.webscraper.scrape()
