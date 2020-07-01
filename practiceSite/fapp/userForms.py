from django import forms
from fapp.models import Users

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'

