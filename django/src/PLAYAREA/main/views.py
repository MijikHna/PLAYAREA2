from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': 'Main Page'})

# Three JS


def test_threejs_001(request):
    return render(request, 'threejs/test-threejs-001.html', {'title': 'Test ThreeJS 001'})


def test_threejs_002(request):
    return render(request, 'threejs/test-threejs-002.html', {'title': 'Test ThreeJS 002'})


def test_threejs_car(request):
    return render(request, 'threejs/test-threejs-car.html', {'title': 'Test ThreeJS Car'})

# Vue


def vue_test_001(request):
    return render(request, 'vue/vue-test-001.html', {'title': 'Test Vue 001'})


def vue_test_002(request):
    return render(request, 'vue/vue-test-002.html', {'title': 'Test Vue 002'})


def vue_test_modal_001(request):
    return render(request, 'vue/vue-test-modal-001.html', {'title': 'Test Vue Modal 001'})


def pure_js_component(request):
    return render(request, 'various/pure-js-component.html', {'title': 'Pure JS Component'})
