"""Semester class for the dualis module"""

import logging

import bs4
from course import Course
from dualis_session import DualisSession

logger = logging.getLogger(__name__)


class Semester:
    """Represents a semester in the dualis system
    """

    def __init__(self, name: str, identifier: str):
        """Constructor

        Args:
            name (str): Semester name (i.e. "WISE 2020/2021")
            id (str): Temporary Semester id (i.e. "000000015108000")
        """
        self._name = name
        self._identifier = identifier

        logger.error("Test")

        self._courses = []

    def getCourses(self) -> list:
        """Returns a list of courses

        Returns:
            list: List of courses
        """
        return self._courses

    def addCourse(self, course: Course):
        """Adds a course to the semester

        Args:
            course (Course): Course to add
        """
        self._courses.append(course)

    def scrapeCourses(self, session: DualisSession) -> list:
        """Scrapes the courses from the dualis system

        Args:
            session (DualisSession): Dualis session

        Returns:
            list: List of courses
        """
        response = session.get(
            "https://dualis.dhbw.de/scripts/mgrqispi.dll" +
            "?APPNAME=CampusNet&PRGNAME=COURSERESULTS" +
            f"&ARGUMENTS=-N{session.getAuthToken()}" +
            f",-N000307,-N{self.getId()},")
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", {"class": "nb list"})

        for row in table.find_all("tr"):
            # print(row)
            try:
                course_number = row.find_all("td", {"class": "tbdata"})[0].text
                course_name = row.find_all("td", {"class": "tbdata"})[1].text
                course_grade = row.find_all(
                    "td", {"class": "tbdata_numeric"})[0].text
                course_credits = row.find_all(
                    "td", {"class": "tbdata_numeric"})[1].text
                self.addCourse(Course(course_number, course_name,
                               course_grade, course_credits))
            except IndexError:
                continue

    def getName(self) -> str:
        """Returns the semester name

        Returns:
            str: Semester name
        """
        return self._name

    def getId(self) -> str:
        """Returns the semester id

        Returns:
            str: Semester id
        """
        return self._identifier

    def __str__(self) -> str:
        """Returns a string representation of the semester

        Returns:
            str: String representation of the semester
        """
        return f"{self._name} ({self._identifier})"
