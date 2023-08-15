from django.contrib import admin

from catalog.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'last_name',)
