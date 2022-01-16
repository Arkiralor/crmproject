from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Questionare(models.Model):
    '''
    Model for questionare.
    '''
    fname = models.CharField(max_length=16)
    lname = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)
    PHONE_VALID = RegexValidator(r'^([0-9]){10}', "Hashtag doesn't comply.")
    phone = models.CharField(max_length=10, validators=[PHONE_VALID])
    COURSE_CHOICES = (
        ('BSc in IT', 'BSc(IT)'),
        ('BSc in CSc', 'BSc(CS)'),
        ('BTech in CSc', 'BTech(CS)'),
        ('BTech in EE', 'BTech(EE)'),
    )
    course = models.CharField(choices=COURSE_CHOICES, max_length=128)
    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.fname+" "+self.lname

