from pathlib import Path
import random

from django.core.management.base import BaseCommand
from django.conf import settings
from students.models import Student

BASE_DIR: Path = settings.BASE_DIR


dummy_names = [
    line.strip()
    for line in (BASE_DIR / "students/management/commands/dummy_names.txt")
    .read_text()
    .splitlines()
]


class Command(BaseCommand):
    help = "Creates dummy students"

    def add_arguments(self, parser):
        parser.add_argument("num_students", nargs=1, type=int)

    def handle(self, *args, **options):
        num_students: int = options["num_students"][0]

        for _ in range(num_students):
            student = dummy_student()
            student.save()


def dummy_student() -> Student:
    student = Student(
        first_name=random.choice(dummy_names),
        last_name=random.choice(dummy_names),
        age=random.randint(7, 20),
    )

    return student
