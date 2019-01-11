from django.urls import path

from . import views

urlpatterns = [
    path('exams/', views.exam_list),
    path('exams/<int:exam_id>/', views.exam),
]
