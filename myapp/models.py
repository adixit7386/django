from django.db import models

class Feature(models.Model):
    # class Meta:
    #     app_label = 'myproject'
    name= models.TextField(max_length=100,default="na")
    details= models.TextField(max_length=500,default="na")
class NewFeature(models.Model):
    name= models.TextField(max_length=100,default="na")
    details= models.TextField(max_length=500,default="na")
# Create your models here.
