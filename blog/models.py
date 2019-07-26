from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def short(self):
        return self.body[:80]

    def __str__(self):
        return self.title

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    comment = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.first_name

    

