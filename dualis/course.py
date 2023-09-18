
class Course:
    """Represents a course in the dualis system
    """

    def __init__(self,
                 course_number: str,
                 name: str,
                 grade: str,
                 credits: str) -> None:
        """Constructor

        Args:
            course_number (str): Course Number
            name (str): Course Name
            grade (str): Course Grade
            credits (str): Course Credits
        """
        self._course_number = course_number
        self._name = name
        self._grade = (float(
            grade.strip().replace(",", "."))
            if "noch nicht gesetzt" not in grade else None)
        self._credits = float(credits.strip().replace(",", "."))

    def getName(self) -> str:
        """Returns the course name

        Returns:
            str: Course name
        """
        return self._name

    def getGrade(self) -> float:
        """Returns the course grade

        Returns:
            float: Course grade
        """
        return self._grade

    def __str__(self) -> str:
        """Returns a string representation of the course

        Returns:
            str: String representation of the course
        """
        return f"{self._course_number} - {self._name} ({self._grade})"
