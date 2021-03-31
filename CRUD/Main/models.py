from django.db import models

# Create your models here.
class Information(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    info_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname