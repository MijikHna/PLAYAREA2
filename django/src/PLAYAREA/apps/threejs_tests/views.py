from django.shortcuts import render

from typing import Dict, Any

from playarea.utils.Helper import Helper


def test_threejs_001(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {}
        context['title'] = 'Test ThreeJS 001'
        context['apps'] = Helper.getAllApps()

        return render(request, 'test-threejs-001.html', context)
    else:
        # TODO: return 403/401
        pass


def test_threejs_002(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {}
        context['title'] = 'Test ThreeJS 002'
        context['apps'] = Helper.getAllApps()

        return render(request, 'test-threejs-002.html', context=context)
    else:
        # TODO: return 403/401
        pass


def test_threejs_car(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {}
        context['title'] = 'Test ThreeJS 002'
        context['apps'] = Helper.getAllApps()

        return render(request, 'test-threejs-car.html', context)
    else:
        # TODO: return 403/401
        pass
