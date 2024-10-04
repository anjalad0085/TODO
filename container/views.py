from django.shortcuts import render, redirect
from .models import Entry
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import EntryForm


def LoginPage(request):
    page = 'login'
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password doesn\'t exist')
            
    context={'page':page}
    return render(request,'container/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            return redirect('home')
        
        else:
            messages.error(request,'An error occured')
            
    return render(request,'container/register.html',{'form':form})

@login_required   
def Home(request):
    entries = Entry.objects.filter(user=request.user)
    context = {'entries':entries}
    return render(request,'container/home.html',context)

def DisplayList(request,pk):
    entry = Entry.objects.get(pk=pk)
    context = {'entry':entry}
    return render(request,'container/display.html',context)

def MarkAsCompleted(request,pk):
    entry = Entry.objects.get(pk=pk)
    if request.method=='POST':
        entry.progress = 'Completed'
        entry.save()
        messages.success(request,'Entry marked as completed!')
        return redirect('home')
    return redirect('home')

@login_required  
def ListCreate(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user 
            entry.save()
            messages.success(request, 'Entry successfully created!')
            return redirect('home')
        else:
            form = EntryForm()            
    context = {'form':form}
    return render(request,'container/form.html',context)

def ListUpdate(request,pk):
    entry = Entry.objects.get(pk=pk)
    form = EntryForm(instance=entry)
    
    if request.method == 'POST':
        form = EntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
 
            
    context = {'form':form}
    return render(request,'container/form.html',context)
    
def ListDelete(request,pk):
    entry = Entry.objects.get(pk=pk)
    if request.method=='POST':
        entry.delete()
        messages.success(request,'Entry Successfully deleted!')
        return redirect('home')
    
    context = {'entry':entry}
    return render(request,'container/confirm_delete.html',context)
