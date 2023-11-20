from django.contrib import admin
from .models import *


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic',)
    list_display_links = ('surname', 'name', 'patronymic',)
    search_fields = ('surname', 'name', 'patronymic',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'grade',)
    list_display_links = ('lesson', 'student', 'grade')
    search_fields = ('lesson', 'student',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'published',)
    list_display_links = ('published',)
    search_fields = ('lesson', 'published',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher',)
    list_display_links = ('teacher',)
    search_fields = ('name', 'teacher',)


admin.site.register(Students, StudentsAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Subject, SubjectAdmin)
