from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Course, Question, Choice, Submission, Enrollment

# View for Course Details
def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})

# Task 5: Submit Exam View
@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        # Get the enrollment for the current user and course
        enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
        
        # If no enrollment exists, you might want to handle it (e.g., auto-enroll or error)
        # For this lab, we will just error out or redirect if not enrolled
        if not enrollment:
            # Optional: Create enrollment on the fly
            # enrollment = Enrollment.objects.create(user=request.user, course=course)
            return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))

        # Create a new submission
        submission = Submission.objects.create(enrollment=enrollment)
        
        # Loop through all questions in the course to find selected choices
        for question in course.question_set.all():
            for choice in question.choice_set.all():
                # Check if this choice ID is in the POST data
                # The HTML form used name="choice_<id>"
                if f"choice_{choice.id}" in request.POST:
                    submission.choices.add(choice)
        
        submission.save()
        
        # Redirect to the result page
        return HttpResponseRedirect(reverse('onlinecourse:submission_result', args=(course.id, submission.id)))

    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})

# Task 5: Show Exam Result View
@login_required
def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Verify the submission belongs to the current user
    if submission.enrollment.user != request.user:
        return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})
    
    context['course'] = course
    context['submission'] = submission
    
    # Calculate score
    total_grade = 0
    score = 0
    
    # Get a list of all selected choice IDs for this submission
    selected_ids = [c.id for c in submission.choices.all()]
    
    for question in course.question_set.all():
        total_grade += question.grade
        # Use the is_get_score method defined in models.py
        if question.is_get_score(selected_ids):
            score += question.grade
            
    context['grade'] = score
    context['total_grade'] = total_grade
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)