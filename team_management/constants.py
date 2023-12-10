from django.db import models


class RoleTypes(models.IntegerChoices):
    REGULAR = 1, "Regular - Can't delete members"
    ADMIN = 2, "Admin - Can delete members"
