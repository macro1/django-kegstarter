from django.conf.urls import patterns, url, include

from .routers import api_router


urlpatterns = patterns('',
    url(r'^v1/', include(api_router.urls, namespace="v1")),
)
