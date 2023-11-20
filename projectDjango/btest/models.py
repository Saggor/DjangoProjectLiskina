from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Школьники
class Students(models.Model):
    surname = models.CharField(null=False, max_length=100, verbose_name='Фамилия')
    name = models.CharField(null=False, max_length=100, verbose_name='Имя')
    patronymic = models.CharField(null=False, max_length=100, verbose_name='Отчетство')

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name_plural = 'Школьники'
        verbose_name = 'Школьник'
        ordering = ['surname']


# Предмет
class Subject(models.Model):
    name = models.CharField(null=False, max_length=100, verbose_name='Название')
    teacher = models.CharField(null=False, max_length=200, verbose_name='Преподатаватель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'


# Занятие
class Lesson(models.Model):
    lesson = models.ForeignKey('Subject', null=False, on_delete=models.PROTECT, verbose_name='Занятие')
    published = models.DateField(blank=False, null=False, verbose_name='Дата')

    def __str__(self):
        return f"{self.lesson.name}, {self.published.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name_plural = 'Занятия'
        verbose_name = 'Занятие'
        ordering = ['published']


# Оценка
class Grade(models.Model):
    lesson = models.ForeignKey('Lesson', null=False, on_delete=models.PROTECT, verbose_name='Занятие')
    student = models.ForeignKey('Students', null=False, on_delete=models.PROTECT, verbose_name='Учащийся')
    grade = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(2), MaxValueValidator(5)],verbose_name='Оценка')

    def __str__(self):
        return str(self.grade)

    class Meta:
        verbose_name_plural = 'Оценки'
        verbose_name = 'Оценка'
        unique_together = ('lesson', 'student')
