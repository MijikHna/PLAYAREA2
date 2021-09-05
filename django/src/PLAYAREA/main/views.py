from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import App, SubApp

from typing import List, Dict, Any
import json

app_name: str = "Main Page"
# Create your views here.


@login_required(login_url='/apps/accounts/login/')
def index(request):
    apps: List[App] = App.objects.all()

    apps_serialized = list(map(lambda x: x.serialize(), apps))
    context: Dict[str, Any] = {
        'title': app_name,
        'js': {
            'apps': json.dumps(apps_serialized)
        }
    }

    return render(request, 'index.html', context)


def getAllApps(request):
    if request.user.is_authenticated:
        from django.core import serializers

        apps: List[App] = App.objects.all()
        apps_serialized = list(map(lambda x: x.serialize(), apps))

        # apps_serialized = json.dumps(json.loads(serializers.serialize('json', apps, fields=('id', 'name', 'href', 'subApps'))), indent=4)

        return JsonResponse(apps_serialized, safe=False)

    return JsonResponse({}, status=403)
