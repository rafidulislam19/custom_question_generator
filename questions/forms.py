from django import forms
from .models import Question

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            if question.question_type == 'radio':
                options = question.options.all()
                choices = [(option.id, option.text) for option in options]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect(attrs={'class': 'radio-option'}),
                    required=True
                )
            elif question.question_type == 'scoring':
                max_score = question.max_score or 10
                choices = [(score, str(score)) for score in range(max_score + 1)]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect(attrs={'class': 'scoring-option'}),
                    required=True
                )
