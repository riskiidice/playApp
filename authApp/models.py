from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your models here.
class UserProfile(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False)
    address = models.TextField()
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    parent_number = models.DecimalField(max_digits=10, decimal_places=10)
    student_number = models.DecimalField(max_digits=10, decimal_places=10)
    old_school = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.owner.first_name + self.group.name