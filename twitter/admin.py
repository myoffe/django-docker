from django.contrib import admin

from . import models

admin.site.register(models.Tweet)
admin.site.register(models.ReTweet)
admin.site.register(models.Like)
