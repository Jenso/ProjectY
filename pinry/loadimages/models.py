from django.db import models

class Feeds(models.Model):
    name = models.CharField("", max_length=80)
    url = models.CharField("", max_length=400)
    # TODO: should be FileField
    filename = models.TextField()
    
class FailedSKUs(models.Model):
    feed = models.ForeignKey(Feeds)
    sku = models.TextField()
    

