from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    text = models.TextField()    
 
    def __str__(self):
        return self.name
    