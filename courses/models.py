from django.db import models
from DRF_homeworks import settings


class Course(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='previews/', null=True, blank=True, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

