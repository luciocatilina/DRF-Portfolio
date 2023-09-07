from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    tools = models.TextField(blank=False, null=False)
    repository = models.TextField(blank=False, null=False)
    host = models.TextField(blank=False, null=False)
    
class SmallProject(Project):

    date = models.DateField()

class BigProject(Project):
    
    date1=models.DateField()
    date2=models.DateField()