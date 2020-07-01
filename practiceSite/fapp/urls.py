from fapp import views
from django.urls import path

app_name = 'fapp'

urlpatterns = [
    path('',views.index, name='index'),
    path('Help',views.Help, name='Help'),
    path('FormPage',views.FormNameView, name='FormName'),
    path('UserPage',views.users,name='UserPage'),
    path('Register',views.Register,name="Register"),
    path('UserLogin',views.UserLogin,name="UserLogin")
]