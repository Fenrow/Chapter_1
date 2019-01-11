from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    #Home page
    path('', views.api_root),
    #List of all exams
    path('exams/', views.Exam_list.as_view(), name='exam-list'),
    #A single exam
    path('exams/<int:pk>/',
        views.Exam_detail.as_view(),
        name='exam-detail'),
    #List of all users
    path('users/', views.UserList.as_view(), name='user-list'),
    #Detail of single user
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
