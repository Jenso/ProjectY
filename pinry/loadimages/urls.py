from django.conf.urls import patterns, include, url
from django.conf import settings
from pinry.loadimages.views import LoadImagesView


urlpatterns = patterns('',
                           (r'^load/$',
            LoadImagesView.as_view(),
            {},
            'index_page'),

)
