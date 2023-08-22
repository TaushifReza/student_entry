from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .forms import StudentForm
from .models import Student

# Create your views here.


def home_page(request):
    student_data = Student.objects.all().order_by("-pk")
    return render(
        request,
        "student/index.html",
        {
            "student_data": student_data,
        },
    )


def student_register_page(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home_page"))
    else:
        form = StudentForm()
    return render(request, "student/student_register.html", {"form": form})


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    print(student)
    student.delete()
    return HttpResponseRedirect(reverse("home_page"))


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home_page"))
    else:
        form = StudentForm(instance=student)

    return render(
        request, "student/update_student.html", {"form": form, "student": student}
    )
