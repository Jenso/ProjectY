from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'', include('pinry.core.urls', namespace='core')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'^api/', include('pinry.api.urls', namespace='api')),
    url(r'^loadimages/', include('pinry.loadimages.urls', namespace='loadimages')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
