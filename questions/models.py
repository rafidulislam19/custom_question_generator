from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('radio', 'Radio Buttons'),
        ('scoring', 'Scoring')
    ]
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='radio')
    max_score = models.PositiveIntegerField(null=True, blank=True, help_text="Max score for scoring questions.")

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


    def __str__(self):
        return self.text

