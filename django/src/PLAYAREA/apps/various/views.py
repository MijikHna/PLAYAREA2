from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json

from apps.various.service.tests_rpc_service import get_all_cars, get_car_byId, create_Car, delete_Car, change_Car
from playarea.utils.Helper import Helper
from playarea.utils.decorators import set_base_context
from apps.various.models import Car

from typing import Dict, Union, Any
# Create your views here.


def pure_js_component(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Pure JS Component',
            'apps': Helper.getAllApps()
        }
        return render(request, 'pure-js-component.html', context)
    else:
        # TODO: return 401/403
        pass


def daterangepicker(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Daterangepicker',
            'apps': Helper.getAllApps()
        }
        return render(request, 'daterangepicker.html', context)
    else:
        # TODO: return 401/403
        pass


def custom_html(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Custom Html',
            'apps': Helper.getAllApps()
        }
        return render(request=request, template_name='custom-html.html', context=context)
    else:
        # TODO: return 401/403
        pass


def test_rpc_1(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Test RPC 1',
            'apps': Helper.getAllApps()
        }
        return render(request, 'test-rpc-1.html', context)
    else:
        # TODO: return 401/403
        pass


def test_rpc_1_all(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            cars_serialized = list(
                map(lambda x: x.serialize(), get_all_cars()))
            return JsonResponse(cars_serialized, safe=False)
        else:
            return JsonResponse({'stauts': 400, 'message': 'Bad Request'}, status=400)
    else:
        statusMessage: Dict[str, Union[int, str]] = {}
        statusMessage['status'] = 401
        statusMessage['message'] = 'Not Authorized'

        return JsonResponse(statusMessage, status=401)


def test_rpc_1_with_id(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            theCar: Car = get_car_byId(id)
            return JsonResponse(theCar.serialize(), safe=False)
        elif request.method == 'PUT':
            changedCar: Car = change_Car(id)
            return changedCar
        elif request.method == 'DELETE':
            deletedCar: Car = delete_Car(id)
            return deletedCar
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseForbidden()


def test_rpc_1_create(request):
    if request.method == 'POST':
        data: Dict(str, str) = json.loads(request.body.decode('utf-8'))
        createdCar: Car = create_Car(data)
        return JsonResponse(createdCar.serialize(), safe=False, status=201)

    return JsonResponse({'stauts': 401, 'message': 'Bad Request'}, status=401)


@login_required
@set_base_context
def css_swipe_animation(request, context):
    return render(request, 'css-swipe-animation.html', context)
