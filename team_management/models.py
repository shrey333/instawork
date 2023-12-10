from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .constants import RoleTypes


# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField("First name of team member", max_length=256)
    last_name = models.CharField("Last name of team member", max_length=256)
    email = models.EmailField("Email of team member", max_length=254)
    phone = PhoneNumberField("Phone number of team member")
    role = models.PositiveSmallIntegerField(
        "Role of team member", choices=RoleTypes.choices, default=RoleTypes.REGULAR
    )
