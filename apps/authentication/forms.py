"""Forms for the authentication app."""
from django import forms


class LoginForm(forms.Form):
    """Login Form

    Takes E-Mail, Password and Rememberme Checkbox
    """
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'DHBW Email',
                   'id': 'email',
                   'type': 'email',
                   'autofocus': True
                   }
        ),
    )
    remember_me = forms.BooleanField(required=False,
                                     initial=False,
                                     widget=forms.CheckboxInput(
                                         attrs={'class': 'form-check-input',
                                                'id': 'remember_me',
                                                'type': 'checkbox',
                                                'role': 'switch'}
                                     ),
                                     )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Dualis Passwort',
                'id': 'password',
                'type': 'password'
            }
        )
    )
