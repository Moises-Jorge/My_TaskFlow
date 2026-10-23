from django.shortcuts import render, redirect
from django.views.generic import View
from . forms import TaskForm
from . models import Task

# Create your views here.
class IndexView(View):
	def get(self, request):
		if (request.user.is_authenticated):
			total_tasks = Task.objects.filter(user=request.user)
			if (total_tasks is not None):
				completed_tasks = []
				uncompleted_tasks = []

				for task in total_tasks:
					if task.completed == True:
						completed_tasks.append(task)
					else:
						uncompleted_tasks.append(task)
			else:
				completed_tasks = None
				uncompleted_tasks = None

			form = TaskForm()
			context = {
				'form': form,
				'completed_tasks': completed_tasks,
				'uncompleted_tasks': uncompleted_tasks,
			}
			return render(request, 'taskflow/index.html', context)
		else:
			return render(request, 'taskflow/index.html')

	def post(self, request):
		if (request.user.is_authenticated):
			total_tasks = Task.objects.filter(user=request.user)
			if (total_tasks is not None):
				completed_tasks = []
				uncompleted_tasks = []

				for task in total_tasks:
					if task.completed == True:
						completed_tasks.append(task)
					else:
						uncompleted_tasks.append(task)
			else:
				completed_tasks = None
				uncompleted_tasks = None

			form = TaskForm(request.POST)
			if (form.is_valid()):
				user = request.user
				task = form.cleaned_data['task']
				completed = False
				new_task = Task.objects.create(user=user, task=task, completed=completed)
				new_task.save()
				return redirect('index')
			else:
				context = {
					'form': form,
					'completed_tasks': completed_tasks,
					'uncompleted_tasks': uncompleted_tasks,
				}
				return render(request, 'taskflow/index.html', context)
		else:
			return render(request, 'taskflow/index.html')
