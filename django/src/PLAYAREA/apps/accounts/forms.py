from .models import Profile
from django.contrib.auth.models import User

from django.utils.translation import gettext
from django.conf import settings

from django.forms import ModelForm, Textarea, FileInput, Select, TextInput, widgets

from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserChangeForm, UserCreationForm


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'autofocus': False})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control'})


class AuthenticationCustomForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super(AuthenticationCustomForm, self).__init__(
            request, *args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserCreationCustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationCustomForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'picture', 'language']
        label = {
            'bio': gettext('Bio'),
            'picture': gettext('Picture'),
            'language': gettext('Language'),
        }

        widgets = {
            'bio': Textarea(attrs={'class': 'form-control'}),
            'picture': FileInput(attrs={'class': 'custom-file-input'}),
            'language': Select(attrs={'class': 'form-control'}, choices=settings.LANGUAGES)
        }
        help_texts = {
            'bio': gettext('Information about you'),
            'picture': gettext('Your picture'),
            'language': gettext('Your Language'),
        }
        error_messages = {
            'bio': {
                'error_1': gettext('test bio'),
            },
            'picture': {
                'error_1': gettext('test picture'),
            },
            'language': {
                'error_1': gettext('test language'),
            },
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


class UserChangeCustomForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(UserChangeCustomForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

        '''
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'})
        }
        '''
