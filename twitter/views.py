import json
from django.http import JsonResponse

from . import models

def list_tweets(request):
    tweets = models.Tweet.objects.all()
    return json_response([t.as_dict() for t in tweets])


def json_response(obj):
    return JsonResponse(obj, safe=False)
