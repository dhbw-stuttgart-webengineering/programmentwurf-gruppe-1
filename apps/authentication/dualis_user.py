from django.contrib.auth.models import User
from ...dualis import Dualis


class DualisUser(User):
    def __init__(self, username: str, password: str):
        super().__init__(username=username, password=password)
        self._is_logged_in = False
        dualis = Dualis(username, password)

    def isLoggedIn(self):
        return self._is_logged_in
