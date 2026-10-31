from django.shortcuts import render, redirect
from django.views.generic import View

class RegisterView(View):
    def get(self, request):
        pass

class ResetPassView(View):
    def get(self, request):
        pass

class RegisterSuccessView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('index')
        return render(request, 'users/register_success.html')

class ResetSuccess(View):
    def get(self, request):
        if (request.user.is_authenticated):
            return render(request, 'users/reset_success.html')
        return redirect('index')
