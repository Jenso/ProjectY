from django.views.generic import View, ListView, CreateView, TemplateView, DetailView
from elementtree.ElementTree import parse
import os
import sys
from pinry.pins.models import Pin, Category
from pinry.loadimages.models import FailedSKUs, Feeds
import celery

@celery.task
def loadfeeds():
    for feed in Feeds.objects.all():
        tree = parse("pinry/loadimages/feedfiles/" + feed.filename)
        elem = tree.getroot()

        # should be dynamically set
        feed = Feeds.objects.get(id=1)

        i = 0
        for el in elem:    
            try:
                # dont add products which already have been added
                sku = el.find("SKU").text
                pin_object = Pin.objects.filter(sku=sku, store=feed)
                
                # product already exist
                if pin_object:
                    continue

                # if product has no category -> mark as failed
                category = el.find("Category").text
                if not category:
                    fail = FailedSKUs(feed=feed, sku=sku)
                    fail.save()
                    continue

                
                category_obj, is_new_obj = Category.objects.get_or_create(name=category)
                
                new_pin = Pin(url=el.find("ImageUrl").text,
                              tracking_url=el.find("TrackingUrl").text,
                              price=el.find("Price").text,
                              product_url=el.find("ProductUrl").text,
                              submitter_id=1,
                              category=category_obj,
                              real_description=el.find("Description").text,
                              name=el.find("Name").text,
                              brand=el.find("Brand").text,
                              sku=sku,
                              store=feed
                              )
                new_pin.save()
            except:
                fail = FailedSKUs(feed=feed, sku=sku)
                fail.save()


class LoadImagesView(TemplateView):
    """
    A search view for all cities. Enables static text instead of dynamically
    loaded data via ajax. Google likes static text better.

    """
    template_name = "load.html"

    def get_context_data(self, **kwargs):
        context = super(LoadImagesView, self).get_context_data(**kwargs)

        loadfeeds.delay()
        return context
