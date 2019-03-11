# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Activity, Position, Performance, Personal, Status, Jobs

from .forms import RegisterActivity, RegisterPosition, RegisterPerformance, RegisterPersonal, RegisterStatus, RegisterJobs

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {})

def activity_view(request):
	fis_act = list(Activity.objects.all())
	context = {
		'activities': fis_act
	}
	return render(request, "home/activities.html", context)

def position_view(request):
	type_position = list(Position.objects.all())
	context = {
		"positions": type_position
	}
	return render(request, "home/position.html", context)

def performance_view(request):
	lvl_perform = list(Performance.objects.all())
	context = {
		"performs": lvl_perform
	}
	return render(request, "home/performance.html", context)

def personal_view(request):
	human = list(Personal.objects.all())
	context = {
		"humans": human
	}
	return render(request, "home/personal.html", context)

def status_view(request):
	stat = list(Status.objects.all())
	context = {
		"stats": stat
	}
	return render(request, "home/status.html", context)

def jobs_view(request):
	job = list(Jobs.objects.all())
	context = {
		"jobs": job
	}
	return render(request, "home/report.html", context)

def registeractivity_view(request):
	form = RegisterActivity()
	context = { 'form': form }
	if request.method == "POST":
		form = RegisterActivity(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']

			new_activity = Activity(name=name, description=description)
			new_activity.save()
	return render(request, "home/registeractivity.html", context)

def registerposition_view(request):
	form = RegisterPosition()
	context = {'form': form }
	if request.method == "POST":
		form = RegisterPosition(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']

			new_position = Position(name=name, description=description)
			new_position.save()
	return render(request, "home/registerposition.html", context)

def registerperformance_view(request):
	form = RegisterPerformance()
	context = {'form': form }
	if request.method == 'POST':
		form = RegisterPerformance(request.POST)
		if form.is_valid():
			perform = form.cleaned_data['perfom']
			description = form.cleaned_data['description']

			new_performance = Performance(perform=perform, description=description)
			new_performance.save()
	return render(request, "home/registerperformance.html", context)

def registerpersonal_view(request):
	form = RegisterPersonal()
	context = { 'form': form }
	if request.method == "POST":
		form = RegisterPersonal(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			performance = form.cleaned_data['performance']
			position = form.cleaned_data['postion']

			new_Personal = Personal(name=name, age=age, performance=performance, postion=position)
			new_Personal.save()
	return render(request, "home/registerpersonal.html", context)

def registerstatus_view(request):
	form = RegisterStatus()
	context = { 'form': form }
	if request.method == "POST":
		form = RegisterStatus(request.POST)
		if form.is_valid():
			status = form.cleaned_data['status']
			description = form.cleaned_data['description']

			new_status = Status(status=status, description=description)
			new_status.save()
	return render(request, "home/registerstatus.html", context)

def registerjobs_view(request):
	reg_employees = list(Personal.objects.all())
	employees_perform = []
	employees_works = []

	for employee in employees_perform:
		total_activity = Report.objects.filter(personal__id=personal.id).count()
		employee_perform = EmployeePerform(employee, count_jobs)
		employee_perfoms.append(employee_perform)

		employee_works_queryset = Jobs.objects.filter(personal__id=personal.id)
		employees_works = WorksEmployee(employee, list(employee_works_queryset))
		employees_work.append(employees_works)
	
	context = {
		'employee_perfoms': employee_perfoms,
		'employees_work': employees_work
	}
	return render(request, "home/report.html", context)

class EmployeePerform:
    def __init__(self, employee, count_jobs):
        self.employee = employee
        self.count_jobs = count_jobs

class WorksEmployee:
    def __init__(self, employee, works):
        self.employee = employee
        self.works = works






