from django.db import models

# Create your models here.
class Dbs(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', blank=True) # Images will be stored in media/my_images/
