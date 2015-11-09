# Create your models here.
from django.db import models


class ProfileStore(models.Model):
    Name = models.CharField(max_length=30)
    Api_string = models.CharField(max_length=200)
    BPic = models.ImageField(upload_to="")

    @property
    def __unicode__(self):
        return self.Name
