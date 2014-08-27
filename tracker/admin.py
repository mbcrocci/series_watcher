from django.contrib import admin
from tracker.models import Serie, Season, Episode
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class EpisodeInLine(NestedTabularInline):
    model = Episode
    fields = ('title', 'summary', )
    extra = 0


class SeasonInLine(NestedStackedInline):
    model = Season
    fields = ('n_episodes', )
    extra = 0

    inlines = [EpisodeInLine, ]


class SerieAdmin(NestedModelAdmin):
    fields = ('title', 'story_line', 'n_seasons')
    inlines = [SeasonInLine, ]


admin.site.register(Serie, SerieAdmin)
