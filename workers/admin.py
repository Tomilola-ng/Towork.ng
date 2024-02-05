from django.contrib import admin

from .models import Job, Worker

admin.site.register(Job)
admin.site.register(Worker)