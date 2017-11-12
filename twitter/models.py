from django.db import models


class Tweet(models.Model):
    class Meta:
        db_table = 'tweets'

    content = models.CharField(max_length=280)
    username = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return self.like_set.count()

    def retweets_count(self):
        return self.retweet_set.count()

    def as_dict(self):
        return dict(
            id=self.id,
            content=self.content,
            username=self.username,
            timestamp=self.timestamp,
            likes_count=self.likes_count(),
            retweets_count=self.retweets_count(),
        )

    def __str__(self):
        return '{}: {}'.format(self.username, self.content)


class Like(models.Model):
    class Meta:
        db_table = 'likes'

    username = models.CharField(max_length=64)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} liked "{}"'.format(self.username, self.tweet)


class ReTweet(models.Model):
    class Meta:
        db_table = 'retweets'

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return dict(
            content=self.tweet.content,
            retweet_user=self.username,
            tweet_id=self.tweet.id,
            tweet_user=self.tweet.username,
            timestamp=self.timestamp,
        )

    def __str__(self):
        return '{} retweeted "{}"'.format(self.username, self.tweet)
