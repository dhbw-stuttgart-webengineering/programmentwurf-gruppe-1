from course import Course
from dualis_session import DualisSession
import bs4


class Semester:
    def __init__(self, name: str, id: str):
        self._name = name
        self._id = id

        self._courses = []

    def getCourses(self) -> list:
        return self._courses

    def addCourse(self, course: Course):
        self._courses.append(course)

    def scrapeCourses(self, session: DualisSession) -> list:
        r = session.get(
            f"https://dualis.dhbw.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=COURSERESULTS&ARGUMENTS=-N{session.getAuthToken()},-N000307,-N{self.getId()},")
        soup = bs4.BeautifulSoup(r.text, "html.parser")

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
        return self._name

    def getId(self) -> str:
        return self._id

    def __str__(self) -> str:
        return f"{self._name} ({self._id})"
