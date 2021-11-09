from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

def update(request, pk):
    #get_user_data = UserModel.objects.get(pk=pk)
    get_user_data = get_object_or_404(UserModel, pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('home')

    context = {'form':form, 'get_user_data':get_user_data}
    return render(request, 'update.html', context)

# Delete
def delete(request, pk):
    #get_user = UserModel.objects.get(pk=pk)
    get_user = get_object_or_404(UserModel, pk=pk)
    get_user.delete()
    messages.error(request, 'User deleted')
    return redirect('home')