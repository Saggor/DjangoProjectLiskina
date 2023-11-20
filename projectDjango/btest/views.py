from django.shortcuts import render
from .models import *


def dnevnik(request):
    grades = Grade.objects.all()
    students = Students.objects.all()

    for student in students:
        print(student.surname)
        for grade in grades:
            if student.id == grade.student.id:
                print(str(grade.lesson) + " " + str(grade.student) + " " + str(grade.grade))

    return render(request, "btest/dnevnik.html", {
        'grades': grades,
        'students': students
    })


def schedule(request):
    lessons = Lesson.objects.all()

    for lesson in lessons:
        print(str(lesson.lesson.name) + " " +
              str(lesson.lesson.teacher) + " " +
              str(lesson.published))

    return render(request, "btest/schedule.html", {
        'lessons': lessons,
    })

