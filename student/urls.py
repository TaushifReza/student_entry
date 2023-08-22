from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("register", views.student_register_page, name="student_register_page"),
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
    path("edit/<int:student_id>/", views.edit_student, name="edit_student"),
]
