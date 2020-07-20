from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name