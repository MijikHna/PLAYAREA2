from django.shortcuts import render
from django.http import JsonResponse

from .models import App, SubApp

from typing import List
import json

# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': 'Main Page'})


def getAllApps(request):
    from django.core import serializers

    apps: List[App] = App.objects.all()
    #apps_serialized = json.dumps(json.loads(serializers.serialize('json', apps, fields=('id', 'name', 'href', 'subApps'))), indent=4)
    apps_serialized = list(map(lambda x: x.serialize(), apps))
    return JsonResponse(apps_serialized, safe=False)
