from django.shortcuts import render, get_object_or_404
from tracker.models import Serie, Episode


def index(request):
    series_list = Serie.objects.all()[:3]
    context = {'series_list': series_list}
    return render(request, 'tracker/index.html', context)


def details(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    return render(request, 'tracker/details.html', {'serie': serie})


def episode(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'tracker/episode.html', {'episode': episode})
