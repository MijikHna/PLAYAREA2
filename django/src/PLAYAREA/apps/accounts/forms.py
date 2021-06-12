from .models import Profile

from django.forms import ModelForm, Textarea, FileInput

from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control'})
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
        fields = ['bio', 'picture']
        label = {'bio': 'Bio', 'picture': 'Picture'}

        widgets = {
            'bio': Textarea(attrs={'class': 'form-control'}),
            'picture': FileInput(attrs={'class': 'custom-file-input'})
        }
        help_texts = {
            # 'bio': _('Information about you'),
            # 'picture': _('Your picture'),
            'bio': 'Information about you',
            'picture': 'Your picture',
        }
        error_messages = {
            'bio': {
                'error_1': 'test bio',
            },
            'picture': {
                'error_1': 'test picture'
            }
        }
    def __init__(self, *args, **kwargs):
      super(ProfileForm, self).__init__(*args, **kwargs)
      self.fields['picture'].required = False
