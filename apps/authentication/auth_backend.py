from .dualis_user import DualisUser


class DualisAuthBackend:

    def authenticate(self, request, username=None, password=None):

        try:
            user = DualisUser(username=username, password=password)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
