import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST, require_GET
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
    tweet = fetch_tweet(tweet_id)
    tweet.like_set.create(username=data['username'])
    return success()


@require_POST
@csrf_exempt
def retweet(request, tweet_id):
    data = json.loads(request.body)
    tweet = fetch_tweet(tweet_id)
    tweet.retweet_set.create(username=data['username'])
    return success()


@require_GET
@csrf_exempt
def retweets(request):
    retweets = ReTweet.objects.all()
    return json_response([x.as_dict() for x in retweets])


def list_tweets(request):
    tweets = Tweet.objects.all()
    return json_response([x.as_dict() for x in tweets])


def create_tweet(request):
    data = json.loads(request.body)
    Tweet(
        username=data['username'],
        content=data['content'],
    ).save()
    return success()


def fetch_tweet(id):
    return Tweet.objects.get(id=id)


def json_response(obj):
    return JsonResponse(obj, safe=False)

def success():
    return JsonResponse({'success': True})
