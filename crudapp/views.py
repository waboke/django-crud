from django.shortcuts import render, redirect
from . models import UserModel
from .forms import UserForm

# Create your views here.
def Home(request):
    usermodel = UserModel.objects.all()
    context = {'usermodel':usermodel}
    return render(request, 'home.html', context)

def AddUser(request): 
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = UserForm()
    context = {'form':form}
    return render(request, 'adduser.html', context)