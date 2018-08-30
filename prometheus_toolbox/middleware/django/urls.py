# -*- coding: utf-8 -*-
from django.conf.urls import url

from .expose import export_to_django_view


metrics_urlpatterns = [
    url(r'^metrics$', export_to_django_view,
        name='prometheus-django-metrics'),
]
