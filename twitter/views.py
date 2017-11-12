import json
from django.http import HttpResponse

def list_tweets(request):
    return HttpResponse('tweets!')
