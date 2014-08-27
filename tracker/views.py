from django.shortcuts import render
from tracker.models import Serie

def index(request):
    series_list = Serie.objects[:3]
    pass
