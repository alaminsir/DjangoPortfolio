from django.db import models

# Create your models here.
class about(models.Model):
    title           = models.CharField(max_length=100,blank=False)
    description     = models.TextField(max_length=800,blank=False)
    image           = models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title