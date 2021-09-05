from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.translation import gettext, activate
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, LoginView

from .forms import AuthenticationCustomForm, PasswordChangeCustomForm, ProfileForm, UserChangeCustomForm, UserCreationCustomForm

from playarea.utils.Helper import Helper

from .models import Profile

from typing import Dict, Any, Tuple
import json

app_name: str = gettext('My Account')
# Create your views here.


def dashboard(request):
    context: Dict[str, Any] = {'title': app_name}
    context['js'] = {
        'apps': json.dumps(Helper.getAllApps(serialized=True))
    }

    form_profile = ProfileForm(
        instance=Profile.objects.get(user=request.user.id))
    form_password = PasswordChangeCustomForm(request.user)
    form_user = UserChangeCustomForm(
        instance=User.objects.get(pk=request.user.id))
    cookies: Dict(str, str) = {}
    if request.method == "GET":
        context['form_profile'] = form_profile
        context['form_password'] = form_password
        context['form_user'] = form_user

    elif request.method == "POST":
        if 'changeProfile' in request.POST:
            form_profile = ProfileForm(
                request.POST,
                request.FILES,
                instance=Profile.objects.get(id=request.user.id)
            )
            if form_profile.is_valid() and form_profile.has_changed():
                if 'language' in form_profile.changed_data:
                    activate(form_profile.data['language'])
                    cookies[settings.LANGUAGE_COOKIE_NAME] = form_profile.data['language']
                form_profile.changed_data
                form_profile.save()
                profile_notifier = {
                    'notifierName': gettext('Profile'),
                    'notifierMessage': gettext('Profile successfully changed'),
                    'result': 'success'
                }
                context['notifier'] = profile_notifier
            else:
                profile_notifier = {
                    'notifierName': gettext('Profile'),
                    'notifierMessage': gettext('Profile not changed'),
                    'result': 'error'
                }
                context['notifier'] = profile_notifier

        elif 'changePassword' in request.POST:
            form_password = PasswordChangeCustomForm(
                request.user,
                request.POST
            )
            if form_password.is_valid():
                form_password.save()
                password_change_notifier = {
                    'notifierName': gettext('Password'),
                    'notifierMessage': gettext('Password successfully changed'),
                    'result': 'success'
                }
                context['notifier'] = password_change_notifier
            else:
                password_change_notifier = {
                    'notifierName': gettext('Password'),
                    'notifierMessage': gettext('Password not changed'),
                    'result': 'error'
                }
                context['notifier'] = password_change_notifier

        elif 'changeUser' in request.POST:
            form_user = UserChangeCustomForm(
                request.POST, instance=request.user)

            if form_user.is_valid() and form_user.has_changed():
                form_user.save()
                user_change_notifier = {
                    'notifierName': gettext('User'),
                    'notifierMessage': gettext('User successfully changed'),
                    'result': 'success'
                }
                context['notifier'] = user_change_notifier
            else:
                user_change_notifier = {
                    'notifierName': gettext('User'),
                    'notifierMessage': gettext('User not changed'),
                    'result': 'error'
                }

                context['notifier'] = user_change_notifier

    context['form_password'] = form_password
    context['form_profile'] = form_profile
    context['form_user'] = form_user

    response = render(request, 'dashboard.html', context)

    for key, value in cookies.items():
        response.set_cookie(key, value)

    return response


def register(request):
    if request.method == 'POST':
        form = UserCreationCustomForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(request.POST.get('next'))

        messages.error(
            request, "Unsuccessful registration. Invalid information.")

    form = UserCreationCustomForm
    return render(request, 'registration/register.html', {'form': form, 'next': '/main/'})


class LoginCustomView(LoginView):
    '''
    login
    '''
    authentication_form = AuthenticationCustomForm
    template_name = 'registration/custom-login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = '/main/'

        return context

    def post(self, request, *args, **kwargs):
        response = super().post(request=request, args=args, kwargs=kwargs)

        if request.user.is_authenticated:
            userProfile: Profile = Profile.objects.get(user=request.user.id)

            if not userProfile.language:
                activate(settings.LANGUAGES[0][0])
                response.set_cookie(
                    settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGES[0][0])
            else:
                activate(userProfile.language)
                response.set_cookie(
                    settings.LANGUAGE_COOKIE_NAME, userProfile.language)
        return response


class LogoutCustomView(LogoutView):
    '''logout'''
    next_page = '/apps/accounts/login'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, args, kwargs)
        response.delete_cookie(settings.LANGUAGE_COOKIE_NAME)

        return response


class PasswordChangeCustomView(PasswordChangeView):
    '''
    change_password
    '''
    form_class = PasswordChangeCustomForm
    template_name = 'registration/custom-password-change.html'
    success_url = '/apps/accounts/password_change/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js'] = {
            'apps': json.dumps(Helper.getAllApps(serialized=True))
        }

        return context


class PasswordChangeDoneCustomView(PasswordChangeDoneView):
    '''
    password_change/done
    '''
    template_name = 'registration/custom-password-change-done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js'] = {
            'apps': json.dumps(Helper.getAllApps(serialized=True))
        }

        return context
