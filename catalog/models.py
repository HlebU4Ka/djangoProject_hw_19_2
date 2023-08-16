from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    avatar = models.ImageField(upload_to='students/', verbose_name='Avatar', **NULLABLE)
    active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name', 'last_name']
