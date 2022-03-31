from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='services/image/')

    def __str__(self):
        return self.title



