from django.conf.urls import url

from feed.views import user_feed

urlpatterns = [
    url(r'(?P<username>\w+)/$', user_feed),
]
