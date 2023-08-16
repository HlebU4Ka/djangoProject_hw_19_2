from django.core.management.base import BaseCommand

from catalog.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {"name": "Petrov", "last_name": 'Ivan'},
            {"name": "Semionov", "last_name": 'Petr'},
            {"name": "Ivanov", "last_name": 'Alex'},
            {"name": "Aleksand", "last_name": 'Zuk'},
        ]

        # for student in student_list:
        #     Student.objects.create(**student)

        student_list_create = []
        for student in student_list:
            student_list_create.append(Student(**student))

        Student.objects.bulk_create(student_list_create)
