from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm

class LoginView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('index')
        form = LoginForm()
        context = { 'form': form }
        return render(request, 'authentication/login.html', context)

    def post(self, request):
        if (request.user.is_authenticated):
            return redirect('index')

        form = LoginForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if (user is not None):
                login(request, user)
                return redirect('index')
            else:
                form.add_error('username', 'Invalid username or password')
                context = { 'form': form }
                return render(request, 'authentication/login.html', context)
        context = { 'form': form }
        return render(request, 'authentication/login.html', context)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')
