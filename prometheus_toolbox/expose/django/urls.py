# -*- coding: utf-8 -*-
from django.conf.urls import url
from .setup import export_to_django_view


urlpatterns = [
    url(r'^metrics$', export_to_django_view,
        name='prometheus-metrics'),
]
