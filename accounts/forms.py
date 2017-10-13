from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
       
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            # 'username',
            'email',
            'password'
            # 'password2'
        ]

    def clean_email2(self):
        password = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')
        # if password != password2:
            # raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email














