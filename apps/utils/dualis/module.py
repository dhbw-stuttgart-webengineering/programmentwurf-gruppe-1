"""Represents a course in the dualis system"""
import json

from .unit import Unit


class Module:
    """Represents a Module in the dualis system
    """

    def __init__(self,
                 id_: str,
                 name: str,
                 semester: str,
                 module_detail_link: str,
                 credits_: str = None,
                 units: list[Unit] = None) -> None:

        self._id = id_
        self._name = name
        self._semester = semester
        self._credits = credits_
        self.module_detail_link = module_detail_link
        self.units = units

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the module

        Returns:
            dict: dictionary representation of the module
        """
        return {
            "id": self._id,
            "name": self._name,
            "semester": self._semester,
            "credits": self._credits,
            "units": [unit.to_dict() for unit in self.units] if self.units else None}

    def get_credits(self) -> float:
        """Returns the credits of the module

        Returns:
            float: Credits
        """

        return self._credits

    def __str__(self) -> str:
        """Returns a string representation of the module

        Returns:
            str: String representation of the module
        """

        return json.dumps(self.to_dict(),
                          indent=4, ensure_ascii=False)

    def __repr__(self) -> str:
        """Returns a string representation of the module

        Returns:
            str: String representation of the module
        """
        return json.dumps(self.to_dict(),
                          indent=4, ensure_ascii=False)
