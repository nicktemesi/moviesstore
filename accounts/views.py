from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
#from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'accounts/register_done.html', {'user': user})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html', {'user': user})
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')
def logout_view(request):
    logout(request)
    return render(request, 'home/index.html', {'message': 'You have been logged out.'})
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html', {'user': request.user})
    else:
        return render(request, 'accounts/login.html', {'error': 'You need to log in first.'})
def register_done(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/register_done.html', {'user': request.user})
    else:
        return render(request, 'accounts/login.html', {'error': 'You need to register first.'})
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return render(request, 'accounts/profile.html', {'user': request.user})
        else:
            form = UserCreationForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})
    else:
        return render(request, 'accounts/login.html', {'error': 'You need to log in first.'})
