from django.db import models

class Words(models.Model):
    name = models.CharField(max_length=250)
    frequency = models.PositiveIntegerField()
    word_length = models.PositiveIntegerField()

    def __str__(self):
        return self.name



