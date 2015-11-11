# Create your models here.
from django.db import models


class ProfileStore(models.Model):

    name = models.CharField(max_length=30)
    api_string = models.CharField(max_length=200)
    bPic = models.ImageField(upload_to='\Apps\FBAPI\static\Backup_Pics', blank=False)

    def __unicode__(self):
            return self.name
