from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from playarea.utils.decorators import set_base_context

# Create your views here.


@login_required
@set_base_context
def vue_test_001(request, context):
    return render(request, 'vue-test-001.html', context)


@login_required
@set_base_context
def vue_test_002(request, context):
    return render(request, 'vue-test-002.html', context)


@login_required
@set_base_context
def vue_test_003(request, context):
    return render(request, 'vue-test-003.html', context)


@login_required
@set_base_context
def vue_test_modal_001(request, context):
    return render(request, 'vue-test-modal-001.html', context)
