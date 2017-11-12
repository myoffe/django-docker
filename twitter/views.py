import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Tweet, ReTweet, Like

@require_http_methods(['GET', 'POST'])
@csrf_exempt
def tweets(request):
    if request.method == 'GET':
        return list_tweets(request)
    else:
        return create_tweet(request)


def list_tweets(request):
    tweets = Tweet.objects.all()
    return json_response([t.as_dict() for t in tweets])


def create_tweet(request):
    data = json.loads(request.body)
    Tweet(
        username=data['username'],
        content=data['content'],
    ).save()
    return HttpResponse()


def json_response(obj):
    return JsonResponse(obj, safe=False)
