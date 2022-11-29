from django.db import models

# Create your models here.

class Actor(models.Model):
    name=models.CharField(max_length=250)
    des=models.TextField()
    image=models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name



