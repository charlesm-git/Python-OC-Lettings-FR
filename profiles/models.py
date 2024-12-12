from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represent the profile of a user.

    Fields :
        user (OneToOneField): One-to-one relationship to Django User class.
        favorite_city (CharField): Favorite city of the user.

    Methods:
        __str__(): Return a string representation of the profile in the format
            "<User.username>"
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
