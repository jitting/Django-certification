from django.contrib import admin
from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Course Details
    path('course/<int:course_id>/', views.course_details, name='course_details'),

    # Task 6: Submit Exam
    path('course/<int:course_id>/submit/', views.submit, name='submit'),

    # Task 6: Exam Result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='submission_result'),
]