from django.db import models

# Create your models here.
class register(model.Models):
    name=models.CharField(max_length=10,null=True,blank=True)
    dob = models.CharField(max_length=30,null=True,blank=True)
    phone = models.CharField(max_length=30,null=True,blank=True)
    password = models.IntegerField()
    
    def __str__(self):
        return self.name