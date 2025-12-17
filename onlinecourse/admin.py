from django.contrib import admin
# Task 2: Import the 7 classes
from .models import Course, Lesson, Instructor, Enrollment, Question, Choice, Submission

# Task 2: Implement ChoiceInline (allows adding choices within a question)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5  # Provides 5 empty slots for choices by default

# Task 2: Implement QuestionAdmin (registers the Question model with ChoiceInline)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

# Task 2: Implement QuestionInline (allows adding questions within a course)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

# Task 2: Implement LessonAdmin (simple admin view for Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Existing LessonInline (likely already there or needed for CourseAdmin)
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# CourseAdmin (Updated to include QuestionInline)
class CourseAdmin(admin.ModelAdmin):
    # Added QuestionInline to the inlines list
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Register all models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)