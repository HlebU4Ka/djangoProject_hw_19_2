from django.db import models

NULLABLE = {'blank': True, 'null': True, 'default': None}


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='avatar', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.name}, {self.last_name}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['name', 'last_name']
