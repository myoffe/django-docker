import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Tweet, ReTweet, Like

@require_http_methods(['GET', 'POST'])
@csrf_exempt
def tweets(request):
    if request.method == 'GET':
        return list_tweets(request)
    else:
        return create_tweet(request)


@require_POST
@csrf_exempt
def likes(request, tweet_id):
    data = json.loads(request.body)
    username = data['username']
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.like_set.create(username=username)
    return success()


@require_POST
@csrf_exempt
def retweets(request, tweet_id):
    pass


def list_tweets(request):
    tweets = Tweet.objects.all()
    return json_response([t.as_dict() for t in tweets])


def create_tweet(request):
    data = json.loads(request.body)
    Tweet(
        username=data['username'],
        content=data['content'],
    ).save()
    return success()


def json_response(obj):
    return JsonResponse(obj, safe=False)

def success():
    return JsonResponse({'success': True})
