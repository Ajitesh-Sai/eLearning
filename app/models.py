from django.db import models
# from django_sqlite3.models import ListCharField
from embed_video.fields import EmbedVideoField

# Create your models here.

class Course(models.Model):
    code= models.IntegerField(blank=True, unique=True)
    name= models.CharField(max_length=100, blank=True)
    description= models.CharField(max_length=200, blank=True)
    image= models.CharField(max_length=50, blank=True)    

    def __str__(self):
        return self.name

class Item(models.Model):
    code= models.IntegerField(Course, default = 0) #foreign key
    name= models.CharField(max_length = 150, default= '')
    position = models.IntegerField(default= 0)
    video = EmbedVideoField() 

    def __str__(self):
        return self.name
