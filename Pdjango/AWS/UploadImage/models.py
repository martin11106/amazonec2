from django.db import models

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImage(models.Model):
    profile_image = models.ImageField(upload_to='images', max_length=254, blank=True, null=True)
    
