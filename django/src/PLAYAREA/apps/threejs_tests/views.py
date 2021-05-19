from django.shortcuts import render

# Create your views here.


def test_threejs_001(request):
    return render(request, 'test-threejs-001.html', {'title': 'Test ThreeJS 001'})


def test_threejs_002(request):
    return render(request, 'test-threejs-002.html', {'title': 'Test ThreeJS 002'})


def test_threejs_car(request):
    return render(request, 'test-threejs-car.html', {'title': 'Test ThreeJS Car'})
