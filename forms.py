from django import forms
from django.contrib.auth.forms import SetPasswordForm,UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer




class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
      

class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs= {'class':'form-control'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    class Meta:
        model=User
        fields=['username','email','password1','password2']   
        
 

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs= {'class':'form-control'})) 
    
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','address','email','mobile']
        widgets={
            'name':forms.TextInput(attrs={ 'class':'form-control'}),
            'address':forms.TextInput(attrs={ 'class':'form-control'}),
            'email':forms.TextInput(attrs={ 'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={ 'class':'form-control'})

        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs= {'class':'form-control'}))



class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField (label='New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField (label='Confirm New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'class': 'form-control'}))
