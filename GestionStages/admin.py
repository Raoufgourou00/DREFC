from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Company)
admin.site.register(Promoter)
admin.site.register(Stage)
admin.site.register(Employee)