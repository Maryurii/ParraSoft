
from django import forms

from .models import Activity, Position, Performance, Personal, Status, Jobs, Project

class RegisterActivity(forms.Form):
	name = forms.CharField(max_length=30, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=128, label="Activities", widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegisterPosition(forms.Form):
	name = forms.CharField(max_length=30, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=128, label="Position", widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegisterPerformance(forms.Form):
	perfom = forms.CharField(max_length=10, label="Performance", widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=128, label="Description", widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegisterPersonal(forms.Form):
	name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'})) 
	age = forms.IntegerField(label="Age", widget=forms.TextInput(attrs={'class': 'form-control'}))
	performance = forms.ModelChoiceField(queryset=Performance.objects.all(), label="Performance", widget=forms.Select(attrs={'class': 'form-control'}))
	position = forms.ModelChoiceField(queryset=Position.objects.all(), label="Position", widget=forms.Select(attrs={'class': 'form-control'}))

class RegisterStatus(forms.Form):
	status = forms.CharField(max_length=15, label="Status", widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=50, label="Description", widget=forms.TextInput(attrs={'class': 'form-control'})) 

class RegisterProject(forms.Form):
	name = forms.CharField(max_length=30, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=200, label="Description", widget=forms.TextInput(attrs={'class': 'form-control'})) 

class RegisterJobs(forms.Form):
	job = forms.CharField(max_length=128, label="Report", widget=forms.TextInput(attrs={'class': 'form-control'}))
	activity = forms.ModelChoiceField(queryset=Activity.objects.all(), label="Activity", widget=forms.Select(attrs={'class': 'form-control'}))
	personal = forms.ModelChoiceField(queryset=Personal.objects.all(), label="Personal", widget=forms.Select(attrs={'class': 'form-control'}))
	status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status", widget=forms.Select(attrs={'class': 'form-control'}))
	project = forms.ModelChoiceField(queryset=Project.objects.all(), label="Project", widget=forms.Select(attrs={'class': 'form-control'}))
	start_date = forms.DateField(label="Start Date", widget=forms.TextInput(attrs={
		'id': 'datetimepickerOne',
		'class': 'form-control',
		'placeholder': 'Start Date'
		}))
	end_date = forms.DateField(label="End Date", widget=forms.TextInput(attrs={
		'id': 'datetimepickerTwo',
		'class': 'form-control',
		'placeholder': 'End Date'
		}))