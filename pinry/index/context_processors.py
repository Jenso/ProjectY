from django.conf import settings  # import the settings file

def django_settings(context):
    return { 'settings': settings }
