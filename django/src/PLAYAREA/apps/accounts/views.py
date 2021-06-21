from django.db.models.query import InstanceCheckMeta
from .models import Profile
from typing import Dict, Any
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, LoginView

from .forms import AuthenticationCustomForm, PasswordChangeCustomForm, ProfileForm, UserChangeCustomForm, UserCreationCustomForm

from playarea.utils.Helper import Helper

# Create your views here.


def dashboard(request):
    context: Dict[str, Any] = {'title': 'My Account'}
    context['apps'] = Helper.getAllApps()

    form_profile = ProfileForm(
        instance=Profile.objects.get(pk=request.user.id))
    form_password = PasswordChangeCustomForm(request.user)
    form_user = UserChangeCustomForm(
        instance=User.objects.get(pk=request.user.id))

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
                # form_profile.user = request.user
                form_profile.save()
                profile_notifier = {
                    'notifierName': 'Profile',
                    'notifierMessage': 'Profile successfully changed',
                    'result': 'success'
                }
                context['notifier'] = profile_notifier
            else:
                profile_notifier = {
                    'notifierName': 'Profile',
                    'notifierMessage': 'Profile not changed',
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
                    'notifierName': 'Password',
                    'notifierMessage': 'Password successfully changed',
                    'result': 'success'
                }
                context['notifier'] = password_change_notifier
            else:
                password_change_notifier = {
                    'notifierName': 'Password',
                    'notifierMessage': 'Password not changed',
                    'result': 'error'
                }
                context['notifier'] = password_change_notifier

        elif 'changeUser' in request.POST:
            form_user = UserChangeCustomForm(
                request.POST, instance=request.user)

            if form_user.is_valid() and form_user.has_changed():
                form_user.save()
                user_change_notifier = {
                    'notifierName': 'User',
                    'notifierMessage': 'User succesfully changed',
                    'result': 'success'
                }
                context['notifier'] = user_change_notifier
            else:
                user_change_notifier = {
                    'notifierName': 'User',
                    'notifierMessage': 'User not changed',
                    'result': 'error'
                }

                context['notifier'] = user_change_notifier

    context['form_password'] = form_password
    context['form_profile'] = form_profile
    context['form_user'] = form_user

    return render(request, 'dashboard.html', context)


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


class LogoutCustomView(LogoutView):
    '''logout'''
    next_page = '/apps/accounts/login'


class PasswordChangeCustomView(PasswordChangeView):
    '''
    change_password
    '''
    form_class = PasswordChangeCustomForm
    template_name = 'registration/custom-password-change.html'
    success_url = '/apps/accounts/password_change/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apps'] = Helper.getAllApps()

        return context


class PasswordChangeDoneCustomView(PasswordChangeDoneView):
    '''
    password_change/done
    '''
    template_name = 'registration/custom-password-change-done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apps'] = Helper.getAllApps()

        return context
