# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Activity, Position, Performance, Personal, Status, Jobs

# Register your models here.

admin.site.register(Activity)
admin.site.register(Position)
admin.site.register(Performance)
admin.site.register(Personal)
admin.site.register(Status)
admin.site.register(Jobs)
