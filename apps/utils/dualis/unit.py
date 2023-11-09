"""Represents a single unit of a module or the module itself"""
import json


class Unit:
    """Represents a single unit of a module or the module itself
    """

    def __init__(self,
                 id_: str,
                 name: str,
                 grade_first_attempt: float,
                 grade_second_attempt: float = None,
                 credits_: float = None) -> None:
        self._id = id_
        self._name = name
        self._grade_first_attempt = grade_first_attempt
        self._grade_second_attempt = grade_second_attempt
        self._credits = credits_

    def set_credit_points(self, credit_points: float):
        """Sets the credit points of the unit

        Args:
            credit_points (float): Credits
        """
        self._credits = credit_points

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the unit

        Returns:
            dict: dictionary representation of the unit
        """
        return {
            "id": self._id,
            "name": self._name,
            "credits": self._credits,
            "grade_first_attempt": self._grade_first_attempt,
            "grade_second_attempt": self._grade_second_attempt
        }

    def get_final_grade(self) -> float:
        """Returns the final grade of the unit. If the second attempt is not set,
        the first attempt is returned.

        Returns:
            float: Grade
        """
        if self._grade_second_attempt:
            return self._grade_second_attempt
        return self._grade_first_attempt

    def __str__(self) -> str:
        return json.dumps(self.to_dict(),
                          indent=4, ensure_ascii=False)

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(),
                          indent=4, ensure_ascii=False)
