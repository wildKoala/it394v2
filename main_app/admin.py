from django.contrib import admin
from .models import Lesson, Assignment, ClassFile
# Register your models here.
admin.site.register(Lesson)

# Added these two models. They should populate on the admin page now.
admin.site.register(Assignment)
admin.site.register(ClassFile)
