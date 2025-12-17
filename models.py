from django.db import models
from django.utils.timezone import now

# ... (Existing Instructor, Course, Lesson, and Enrollment models should be above here) ...

# Question Model
class Question(models.Model):
    # Foreign key to the course this question belongs to
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # The text of the question
    content = models.CharField(max_length=200)
    # The grade/score for this specific question
    grade = models.IntegerField(default=50)

    def __str__(self):
        return "Question: " + self.content

    # Helper method to check if a question is answered correctly
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False

# Choice Model
class Choice(models.Model):
    # Foreign key to the Question this choice belongs to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # The text of the choice option
    content = models.CharField(max_length=200)
    # Boolean to check if this choice is the correct answer
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return "Choice: " + self.content + " (" + str(self.is_correct) + ")"

# Submission Model
class Submission(models.Model):
    # Foreign key to the Enrollment (identifies the student and the course)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    # Many-to-Many relationship because a submission consists of multiple choices selected
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return "Submission: " + str(self.enrollment)