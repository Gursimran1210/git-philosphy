from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
    body = models.TextField(null=True)

    def __str__(self):
        return self.summary

    def short(self):
        return self.body[:150]




