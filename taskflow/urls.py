from django.urls import path
from .views import IndexView, ConcludeView, DeleteView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('conclude/<int:task_id>', ConcludeView.as_view(), name='conclude'),
    path('delete/<int:task_id>', DeleteView.as_view(), name='delete'),
]
