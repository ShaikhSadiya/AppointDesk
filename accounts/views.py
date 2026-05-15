from django.shortcuts import render, redirect
from  django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signup_view(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Account Created Successfully'
            )
           # return HttpResponse("signup successfully")
            return redirect('/login/')

    template_name = 'accounts/signup.html'
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(
                request,
                'Login Successful'
            )

            #return HttpResponse("Login...")
            return redirect('/appointments/')
        else:
            messages.error(
                request,
                'Invalid Username or Password'
            )

    template_name = 'accounts/login.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    messages.info(
        request,
        'Logout Successful'
    )
    return redirect('/')