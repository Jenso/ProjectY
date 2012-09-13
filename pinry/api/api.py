# coding:utf-8
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth.models import User

from pinry.pins.models import Pin

from tastypie.constants import ALL, ALL_WITH_RELATIONS
class PinResource(ModelResource):  # pylint: disable-msg=R0904

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PinResource, self).build_filters(filters)

        # FIXME: unsafe? .. Should be some validation that it's at correct list
        if filters.has_key('category') and filters['category'] != "[]":
            import json
            orm_filters["category__name__in"] = json.loads(filters['category'])
        return orm_filters

    class Meta:
        queryset = Pin.objects.order_by('?')
        resource_name = 'pin'
        include_resource_uri = False
        filtering = {
            'published': ['gt'],
            "category": (ALL_WITH_RELATIONS)
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
