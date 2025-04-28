from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserForm
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserForm,CustomLoginForm

def registrationForm(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)

        if(form.is_valid()):
            form.save()

            messages.success(request, "Reistration successful.you can now Log in.")
            return redirect('user:login')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request,f"{field}: {error}")

            
    else:
        form = CustomUserForm()

    return render(request, 'user/register.html', {'form':form})



def Userlogin(request):
    form = CustomLoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('book:book_list')
            else:
                messages.error(request, "Invalid Email or Password.")


    return render(request,'user/login.html',)