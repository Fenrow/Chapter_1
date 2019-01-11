from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('exams/', views.exam_list),
    path('exams/<int:exam_id>/', views.exam),
]

urlpatterns = format_suffix_patterns(urlpatterns)
