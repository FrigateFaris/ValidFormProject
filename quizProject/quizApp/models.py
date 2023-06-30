from django.core import validators
from django.db import models


# Create your models here.
class Quiz(models.Model):
    user_name = models.CharField(validators=[validators.MinLengthValidator(2)], max_length=20, null=True)
    user_surname = models.CharField(validators=[validators.MinLengthValidator(2)], max_length=20, null=True)
    user_nick = models.CharField(validators=[validators.MinLengthValidator(5)], max_length=30, null=True)
    user_email = models.CharField(validators=[validators.EmailValidator()],  max_length=30, null=True)
    user_date = models.DateField(null=True)
    user_visit = models.CharField(max_length=40, null=True)
    why_we = models.TextField(null=True)
    why_filial = models.TextField(null=True)
    computer_work = models.TextField(null=True)
    administration_work = models.CharField(max_length=4, null=True)

    def __str__(self):
        return f'{self.user_name} - {self.user_surname} - {self.user_email} - {self.user_visit}'
