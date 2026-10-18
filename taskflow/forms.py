from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(
		max_length=100,
		required=True,
		widget=forms.TextInput(attrs={
			'id': 'task_id',
			'class': 'form-control',
			'placeholder': 'enter your task...',
		})
	)
