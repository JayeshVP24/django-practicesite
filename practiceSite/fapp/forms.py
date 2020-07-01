from django import forms
from django.core import validators
from django.contrib.auth.models import User
from fapp.models import UserInfo


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label="Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        allCleanData = super().clean()
        email = allCleanData['email']
        vmail = allCleanData['verifyEmail']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")
        
    # def clean_botCatcher(self):
    #     botCatcher = self.cleaned_data['botCatcher']
    #     if len(botCatcher) > 0:
    #         raise forms.ValidationError("GOTCHA DUMBOOO")
    #  

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserPPForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('portfolio', 'pic')