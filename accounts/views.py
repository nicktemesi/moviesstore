from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@csrf_protect
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


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or 'accounts:profile'
            return redirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'home/index.html', {'message': 'You have been logged out.'})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def register_done(request):
    return render(request, 'accounts/register_done.html', {'user': request.user})


@login_required
@csrf_protect
def edit_profile(request):
    # NOTE: UserCreationForm is not the correct form for editing users.
    # You should use a custom form or UserChangeForm.
    from django.contrib.auth.forms import UserChangeForm  # Better suited for editing

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/profile.html', {'user': request.user})
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})
