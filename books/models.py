from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    publicated_at = models.DateField()

    def __str__(self):
        return self.title