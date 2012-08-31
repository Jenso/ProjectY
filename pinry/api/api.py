# coding:utf-8
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth.models import User

from pinry.pins.models import Pin

from tastypie.constants import ALL, ALL_WITH_RELATIONS
class PinResource(ModelResource):  # pylint: disable-msg=R0904
    """
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PinResource, self).build_filters(filters)
        #import pdb;pdb.set_trace()
        orm_filters["category__name"] = "Speedos"
        return orm_filters
    """
    class Meta:
        queryset = Pin.objects.filter(category__name__in=["Midiklänningar", "Basklänningar", "Maxiklänningar", "Miniklänningar", "Klänningar", "Minikjolar", "Midikjolar"])
        #queryset = Pin.objects.all()
        resource_name = 'pin'
        include_resource_uri = False
        filtering = {
            'published': ['gt'],
            #"category": (ALL_WITH_RELATIONS), SHOULD FRIGGIN WORK, BUT IT DONT :(
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
