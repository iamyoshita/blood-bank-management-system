from django.db import models

# Create your models here.
class cover(models.Model):
        info= models.CharField(max_length=100)
        pic=models.CharField(max_length=500)

        def __str__(self):
            return self.info


