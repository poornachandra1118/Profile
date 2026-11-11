from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student_profile)

admin.site.register(Employee_profile)

admin.site.register(parent)
admin.site.register(Student)
admin.site.register(Employee)

admin.site.register(Project_info)
# admin.site.register(Placement)
# admin.site.register(parent1)
admin.site.register(Applicants)
admin.site.register(JobApplication)
