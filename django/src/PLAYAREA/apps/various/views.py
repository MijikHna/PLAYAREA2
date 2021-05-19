from django.http.response import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render

import json

from apps.various.service.tests_rpc_service import get_all_cars, get_car_byId, create_Car, delete_Car, change_Car
from apps.various.models import Car
# Create your views here.


def pure_js_component(request):
    return render(request, 'pure-js-component.html', {'title': 'Pure JS Component'})


def daterangepicker(request):
    return render(request, 'daterangepicker.html', {'title': 'Daterangepicker'})

def test_rpc_1(request):
    return render(request, 'test-rpc-1.html', {'title': 'Test RPC 1'})

def test_rpc_1_all(request):
    if request.method == 'GET':
        cars_serialized = list(map(lambda x: x.serialize(), get_all_cars()))
        return JsonResponse(cars_serialized, safe=False)

    return HttpResponseBadRequest('URL not found')


def test_rpc_1_with_id(request, id):
    if request.method == 'GET':
        theCar: Car = get_car_byId(id)
        return JsonResponse(theCar.serialize(), safe=False)
    elif request.method == 'PUT':
        changedCar: Car = change_Car(id)
        return changedCar
    elif request.method == 'DELETE':
        deletedCar: Car = delete_Car(id)
        return deletedCar
    
    return HttpResponseBadRequest()

def test_rpc_1_create(request):
    if request.method == 'POST':
        data: Dict(str, str) = json.loads(request.body.decode('utf-8'))
        createdCar: Car = create_Car(data)
        return JsonResponse(createdCar.serialize(), safe=False, status=201)

    return JsonResponse({'stauts': 401, 'message': 'Bad Request'}, status=400)