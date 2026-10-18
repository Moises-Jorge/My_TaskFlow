from django.shortcuts import render
from django.views.generic import View
from . forms import TaskForm

# Create your views here.
class IndexView(View):
	def get(self, request):
		form = TaskForm()
		context = {
			'form': form,
		}
		return render(request, 'taskflow/index.html', context)
