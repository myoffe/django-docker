from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tweets$', views.list_tweets),
]
