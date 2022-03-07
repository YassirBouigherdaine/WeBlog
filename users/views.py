from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm , ProfileUpdateForm, UserUpdateForm




def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  
            messages.success(request, f'{username} your account has been successfully created') 
            return redirect('login')
    else:    
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account has been updated')
            return redirect('user_profile')
    else:
         user_form = UserUpdateForm(instance=request.user)
         profile_form = ProfileUpdateForm(instance=request.user.profile)

    context= {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'users/user_profile.html', context)