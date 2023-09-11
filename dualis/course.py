class Course:
    def __init__(self,
                 course_number: str,
                 name: str,
                 grade: str,
                 credits: str) -> None:
        self._course_number = course_number
        self._name = name
        self._grade = (float(
            grade.strip().replace(",", "."))
            if "noch nicht gesetzt" not in grade else None)
        self._credits = float(credits.strip().replace(",", "."))

    def getName(self) -> str:
        return self._name

    def getGrade(self) -> float:
        return self._grade

    def __str__(self) -> str:
        return f"{self._course_number} - {self._name} ({self._grade})"
