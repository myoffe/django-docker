from django.db import models


class Tweet(models.Model):
    class Meta:
        db_table = 'tweets'

    content = models.CharField(max_length=280)
    username = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return dict(
            id=self.id,
            content=self.content,
            username=self.username,
            timestamp=self.timestamp,
        )

    def __str__(self):
        return '{}: {}'.format(self.username, self.content)


class Like(models.Model):
    class Meta:
        db_table = 'likes'

    username = models.CharField(max_length=64)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class ReTweet(models.Model):
    class Meta:
        db_table = 'retweets'

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
