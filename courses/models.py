from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='previews/', null=True, blank=True, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson_prewivews/', null=True, blank=True, verbose_name='Превью')
    link = models.URLField(verbose_name='Ссылка')
