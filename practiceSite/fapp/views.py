from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fapp.models import Topic, Webpage, AccessRecord, Users
from . import forms
from fapp.userForms import NewUserForm
from fapp.forms import UserInfoForm,UserPPForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    webPgList = AccessRecord.objects.order_by('date')
    dateDict = {'accessRecords':webPgList}
    return render(request, 'fapp/index.html', context=dateDict)

def Help(request):
    dic = {'help':'You at help page bud'}
    return render(request, 'fapp/Help.html', context=dic)

def FormNameView(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request, 'fapp/formPage.html',context={'form':form})

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'fapp/users.html',{'form':form})

def Register(request):
    registered = False

    if request.method == "POST":
        userForm = UserInfoForm(data=request.POST)
        profileForm = UserPPForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']

            profile.save()

            registered = True
        
        else:
            print(userForm.errors, profileForm.errors)
    else:
        userForm =  UserInfoForm()
        profileForm = UserPPForm()

    return render(request, 'fapp/registration.html',{
        'userForm':userForm,
        'profileForm':profileForm,
        'registered':registered
    })

@login_required()
def special(request):
    return HttpResponse("You are logged in, Nice!!")

@login_required()
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    else:
        return render(request, 'fapp/login.html',{})