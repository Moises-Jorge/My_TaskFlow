from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import MyUserCreationForm, MyPasswordChangeForm

class RegisterView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('index')

        form = MyUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        if (request.user.is_authenticated):
            return redirect('index')

        form = MyUserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('register_success')
        
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)

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
