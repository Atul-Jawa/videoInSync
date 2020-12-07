
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.db import transaction
from django.contrib.auth import authenticate



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'your_name',
                'placeholder': 'Your Name',
                'name': 'your_name'
            }
        )
    )
    password = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(
            attrs={
                'id': 'your_pass',
                'placeholder': 'Password',
                'name': 'your_pass'
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is not None and password:
            user = authenticate(username=username, password=password)
            if user is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None
                if user_temp and not user_temp.is_active:
                    email = user_temp.email
                    raise forms.ValidationError(f"Account is not active, you need to activate your account before login. An account activation link has been sent to your mailbox. {email} ")
                raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class CustomUserCreationForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', "password1", "password2", 'image')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'id': 'your_name', 'placeholder': 'Your Name', 'name': 'your_name'})
        self.fields['email'].widget.attrs.update({'id': 'email', 'placeholder': 'Your Email', 'name': 'email'})
        self.fields['password1'].widget.attrs.update({'id': 'your_pass', 'placeholder': 'Password', 'name': 'your_pass'})
        self.fields['password2'].widget.attrs.update({'id': 'your_pass2', 'placeholder': 'Repeat your Password', 'name': 'your_pass'})
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-line', 'style':"display: none;"})
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, image, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.image = image
        user.is_active = True
        if commit:
            user.save()
        return user