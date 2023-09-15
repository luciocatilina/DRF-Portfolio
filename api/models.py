from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    image = models.ImageField(upload_to= 'images', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    tools = models.TextField(blank=False, null=False)
    repository = models.TextField(blank=False, null=False)
    host = models.TextField(blank=True, null=True)
    
class SmallProject(Project):

    date = models.DateField()

class BigProject(Project):
    
    date1=models.DateField()
    date2=models.DateField()