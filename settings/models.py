from django.db import models

# Create your models here.

class biomodel(models.Model):
    currentuser = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.bio 

class appearance(models.Model):
    currentuser = models.CharField(max_length = 50)
    colortheme = models.CharField(max_length = 50)

    def __str__(self):
        return self.colortheme