"""Dualis class"""

import logging

import bs4
from .dualis_session import DualisSession
from .semester import Semester
from .exceptions import InvalidUsernameorPasswordException, NoUsernameorPasswordException

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

    def getGrades(self) -> list:
        """Prints the grades

        Returns:
            list: List of grades
        """
        for semester in self._getSemesterList():
            logger.debug(semester.getId())
            semester.scrapeCourses(self.session)

            for course in semester.getCourses():
                logger.debug(course)

    def _getSemesterList(self) -> list:
        """Returns a list of semester objects

        Returns:
            list: List of semester objects
        """
        response = self.session.get(
            "https://dualis.dhbw.de/scripts/mgrqispi.dll?" +
            "APPNAME=CampusNet&PRGNAME=COURSERESULTS&" +
            f"ARGUMENTS=-N{self.session.getAuthToken()},-N000307,")
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        semester_list = []

        for option in soup.find_all("option"):
            semester_list.append(Semester(option.text, option["value"]))

        return semester_list


if __name__ == "__main__":

    import logging.config

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s.%(module)s: %(message)s")
