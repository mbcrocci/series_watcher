from django.db import models


class Serie(models.Model):
    title = models.CharField(max_length=120)
    story_line = models.CharField(max_length=200)
    n_seasons = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Season(models.Model):
    serie = models.ForeignKey(Serie)
    n_episodes = models.IntegerField()


class Episode(models.Model):
    season = models.ForeignKey(Season)
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title
