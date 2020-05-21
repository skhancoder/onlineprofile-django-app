from django.db import models

# Create your models here.

class linksave(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    currentuser = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.title 