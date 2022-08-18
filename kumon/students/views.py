from django.http import HttpResponse
from django.views import generic

from .models import Student


class StudentListView(generic.ListView):
    template_name = "student_list_view.html"
    model = Student
    context_object_name = "students"
