from django.db import models

class Feeds(models.Model):
    name = models.CharField("Storename", max_length=80)
    url = models.CharField("Url to feed", max_length=400)
    # TODO: should be FileField
    filename = models.TextField("Feed xml-filename")
    
class FailedSKUs(models.Model):
    feed = models.ForeignKey(Feeds)
    sku = models.TextField()
    

