"""User Manager"""
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    """User Manager"""

    def _create_user(self, email: str, password: str, is_staff: bool, is_superuser: bool, **extra_fields):
        """Creates a User

        Args:
            email (str): User E-Mail
            password (str): User Password
            is_staff (bool): True if Staff
            is_superuser (bool): True if Superuser

        Raises:
            ValueError: raised if e-mail not given

        Returns:
            user: User object
        """
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """Creates a User.

        Args:
            email (str): EMail
            password (str): Password

        Returns:
            User: Instance of DualisUser
        """

        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Creates a superuser.

        Args:
            email (str): EMail
            password (str): Password

        Returns:
            User: Instance of DualisUser
        """
        user = self._create_user(email, password, True, True, **extra_fields)
        return user
