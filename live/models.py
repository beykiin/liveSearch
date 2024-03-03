from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.name