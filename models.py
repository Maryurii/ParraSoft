# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Activity(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=128)

	class Meta:
		verbose_name_plural = "Activities"

class Position(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=128)

	class Meta:
		verbose_name_plural = "Positions"

class Performance(models.Model):
	perform = models.CharField(max_length=10)
	description = models.CharField(max_length=128)

	class Meta:
		verbose_name_plural = "Performances"

class Personal(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Personals"

class Status(models.Model):
	status = models.CharField(max_length=15)
	description = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Statuss"

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default="")

    class Meta:
        verbose_name_plural = "Projects"

class Jobs(models.Model):
	job = models.CharField(max_length=128)
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
	personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	class Meta:
		verbose_name_plural = "Jobs"


