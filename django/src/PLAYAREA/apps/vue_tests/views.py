from django.shortcuts import render

# Create your views here.


def vue_test_001(request):
    return render(request, 'vue-test-001.html', {'title': 'Test Vue 001'})


def vue_test_002(request):
    return render(request, 'vue-test-002.html', {'title': 'Test Vue 002'})


def vue_test_003(request):
    return render(request, 'vue-test-003.html', {'title': 'Test Vue 003'})


def vue_test_modal_001(request):
    return render(request, 'vue-test-modal-001.html', {'title': 'Test Vue Modal 001'})
