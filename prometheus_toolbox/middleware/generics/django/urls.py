from django.conf.urls import url
from prometheus_toolbox.middleware.generics.django.exports import export_to_django_view


urlpatterns = [
    url(r'^metrics$', export_to_django_view,
        name='prometheus-django-metrics'),
]
