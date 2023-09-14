"""Exceptions used in the dualis package."""


class NoUsernameorPasswordException (Exception):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="No username or password provided"):
        self.message = message
        super().__init__(self.message)
