from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tweets$', views.tweets),
    url(r'^retweets$', views.retweets),
    url(r'^tweets/(?P<tweet_id>[0-9]+)/likes', views.likes),
    url(r'^tweets/(?P<tweet_id>[0-9]+)/retweet', views.retweet),
]
