from django.shortcuts import render

from typing import Dict, List, Any

from main.models import App
from playarea.utils.Helper import Helper
# Create your views here.


def excel_clone(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Excel Clone',
            'apps': Helper.getAllApps()
        }

        return render(request, 'excel-clone.html', context)
    else:
        # TODO: return 401/403
        pass
