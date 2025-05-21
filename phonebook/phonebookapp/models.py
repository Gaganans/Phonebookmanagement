from django.db import models

# Create your models here.
class phonebook1(models.Model):
    Name=models.CharField(max_length=20)
    Number=models.IntegerField()

def __str__(self):
    return self.Name()    