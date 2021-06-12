from django.shortcuts import render

from typing import Dict, Any

from playarea.utils.Helper import Helper


def index(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {}
        context['title'] = 'Karnevalsorden Editor'
        context['apps'] = Helper.getAllApps()

        return render(request, 'karnevalsorden_editor.html', context)
    else:
        # TODO: return 403/401
        pass
