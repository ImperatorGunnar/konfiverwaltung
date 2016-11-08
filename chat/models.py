from django.db import models

# Create your models here.

class Sonn(models.Model):
    kirche = models.TextField()
    datum = models.DateTimeField()
    konfi = models.TextField(null=True)

