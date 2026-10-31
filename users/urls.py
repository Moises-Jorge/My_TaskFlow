from django.urls import path
from .views import RegisterView, RegisterSuccessView, ResetPassView, ResetSuccess

urlpatterns = [
	path('register', RegisterView.as_view(), name='register'),
	path('register_success', RegisterSuccessView.as_view(), name='register_success'),
	path('reset_pass', ResetPassView.as_view(), name='reset_pass'),
	path('reset_success', ResetSuccess.as_view(), name='reset_success'),
]

