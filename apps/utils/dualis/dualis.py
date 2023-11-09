"""Dualis class"""

import logging

from .dualis_session import DualisSession
from .webscraper import WebScraper
from .module import Module
from .unit import Unit

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

        self.username = username

        if self.username == "example@lehre.dhbw-stuttgart.de":
            return
        self.session = DualisSession(username, password)
        self.webscraper = WebScraper(session=self.session)

    def get_name(self) -> str:
        """Returns the name of the user

        Returns:
            str: Name of the user
        """

        if self.username == "example@lehre.dhbw-stuttgart.de":
            return "Max Mustermann"

        return self.webscraper.scrape_username()

    def get_grades(self) -> list:
        """Return a List of Module Objects that contain all Units

        Returns:
            list: List of Module Objects
        """

        if self.username == "example@lehre.dhbw-stuttgart.de":
            return [Module("T3INF2003", "Software Engineering I", "SoSe 2024", "", 9.0, [Unit("T3INF2003", "Software Engineering I", None, None, 9.0)]), Module("T3INF2004", "Datenbanken", "SoSe 2024", "", 6.0, [Unit("T3INF2004", "Datenbanken", None, None, 6.0)]), Module("T3INF2001", "Mathematik II", "WiSe 2023/24", "", 6.0, [Unit("T3INF2001.1", "Angewandte Mathematik", None, None, 6.0)]), Module("T3INF2002", "Theoretische Informatik III", "WiSe 2023/24", "", 6.0, [Unit("T3INF2002", "Theoretische Informatik III", None, None, 6.0)]), Module("T3INF2006", "Kommunikations- und Netztechnik", "WiSe 2023/24", "", 5.0, [Unit("T3INF2006", "Kommunikations- und Netztechnik", None, None, 5.0)]), Module("T3INF4221", "Einsatz von Webtechnologien", "WiSe 2023/24", "", 5.0, [Unit("T3INF4221", "Einsatz von Webtechnologien", None, None, 5.0)]), Module("T3_1000", "Praxisprojekt I", "SoSe 2023", "", 20.0, [Unit("T3_1000.1", "Projektarbeit 1", 1.0, None, 10.0), Unit("T3_1000.2", "Wissenschaftliches Arbeiten 1", None, None, 10.0)]), Module("T3INF1001", "Mathematik I", "SoSe 2023", "", 8.0, [Unit("T3INF1001.1", "Lineare Algebra", 2.8, None, 4.0), Unit("T3INF1001", "Analysis", 3.8, None, 4.0)]), Module("T3INF1003", "Theoretische Informatik II", "SoSe 2023", "", 5.0, [Unit("T3INF1003", "Theoretische Informatik II", 2.9, None, 5.0)]), Module("T3INF1004", "Programmieren", "SoSe 2023", "", 9.0, [Unit("T3INF1004", "Programmieren", 2.9, None, 9.0)]), Module("T3INF4101", "Web Engineering", "SoSe 2023", "", 3.0, [Unit("T3INF4101", "Web Engineering", 2.1, None, 3.0)]), Module("T3INF4103", "Anwendungsprojekt Informatik", "SoSe 2023", "", 5.0, [Unit("T3INF4103", "Anwendungsprojekt Informatik", 2.0, None, 5.0)]), Module("T3INF4190", "Schlüsselqualifikationen II", "SoSe 2023", "", 5.0, [Unit("T3INF4190", "Schlüsselqualifikationen II", 1.8, None, 5.0)]), Module("T3INF1001", "Mathematik I", "WiSe 2022/23", "", 8.0, [Unit("T3INF1001.1", "Lineare Algebra", 2.8, None, 4.0), Unit("T3INF1001", "Analysis", 4.8, 1.0, 4.0)]), Module("T3INF1002", "Theoretische Informatik I", "WiSe 2022/23", "", 5.0, [Unit("T3INF1002", "Theoretische Informatik I", 2.3, None, 5.0)]), Module("T3INF1005", "Schlüsselqualifikationen", "WiSe 2022/23", "", 5.0, [Unit("T3INF1005", "Schlüsselqualifikationen (STG-TINF22E)", 4.7, 3.1, 5.0)]), Module("T3INF1006", "Technische Informatik I", "WiSe 2022/23", "", 5.0, [Unit("T3INF1006", "Technische Informatik I", 1.1, None, 5.0)])]  # pylint: disable=line-too-long

        return self.webscraper.scrape()
