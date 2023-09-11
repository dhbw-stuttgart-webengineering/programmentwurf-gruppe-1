import confidential_settings
from dualis_session import DualisSession
import bs4
from semester import Semester


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
            print(semester.getId())
            semester.scrapeCourses(self.session)

            for course in semester.getCourses():
                print(course)

    def _getSemesterList(self) -> list:
        """Returns a list of semester objects

        Returns:
            list: List of semester objects
        """
        r = self.session.get(
            "https://dualis.dhbw.de/scripts/mgrqispi.dll?" +
            "APPNAME=CampusNet&PRGNAME=COURSERESULTS&" +
            f"ARGUMENTS=-N{self.session.getAuthToken()},-N000307,")
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        semester_list = []

        for option in soup.find_all("option"):
            semester_list.append(Semester(option.text, option["value"]))

        return semester_list


if __name__ == "__main__":
    dualis = Dualis(confidential_settings.EMAIL, confidential_settings.PASSWD)
    dualis.getGrades()
