from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import User
from pinry.loadimages.models import Feeds

import urllib2
import os
from PIL import Image

class Category(models.Model):
    name = models.CharField("Category name", max_length=80)


class Pin(models.Model):
    submitter = models.ForeignKey(User)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    real_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pins/pin/originals/')
    thumbnail = models.ImageField(upload_to='pins/pin/thumbnails/')
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    price = models.IntegerField(max_length=20, blank=True, null=True)
    tracking_url = models.TextField(blank=True, null=True)
    product_url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)
    store = models.ForeignKey(Feeds, null=True, blank=True)
    

    def __unicode__(self):
        return self.url


    def save(self, *args, **kwargs):
        hash_name = os.urandom(32).encode('hex')

        if not self.image:
            temp_img = NamedTemporaryFile()
            temp_img.write(urllib2.urlopen(self.url).read())
            temp_img.flush()
            image = Image.open(temp_img.name)
            image.save(temp_img.name, 'JPEG')
            self.image.save(''.join([hash_name, '.jpg']), File(temp_img))

        if not self.thumbnail:
            if not self.image:
                image = Image.open(temp_img.name)
            else:
                super(Pin, self).save()
                from django.core.files.storage import default_storage
                image = Image.open(default_storage.open(self.image.name))
            size = image.size
            prop = 200.0 / float(image.size[0])
            size = (int(prop*float(image.size[0])), int(prop*float(image.size[1])))
            image.thumbnail(size, Image.ANTIALIAS)
            temp_thumb = NamedTemporaryFile()
            image.save(temp_thumb.name, 'JPEG')
            self.thumbnail.save(''.join([hash_name, '.jpg']), File(temp_thumb))

        super(Pin, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-id']
