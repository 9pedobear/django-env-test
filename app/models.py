from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(
        max_length=222
    )
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)