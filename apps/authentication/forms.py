from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Email',
                   'autofocus': True,
                   'id': 'email'}),
    )
    rememberme = forms.BooleanField(required=False,
                                    initial=False,
                                    widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check-input'}),
                                    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Dualis Passwort',
                'class': 'form-control',
                'id': 'password'
            }
        ))
