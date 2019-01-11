from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('exams/', views.Exam_list.as_view()),
    path('exams/<int:pk>/', views.Exam_instance.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
