from django.shortcuts import render
from .forms import QuestionForm

def question_list(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            
            answers = {}
            for key, value in form.cleaned_data.items():
                question_id = int(key.split('_')[1])
                answers[question_id] = value
            
            print(answers)

            form = QuestionForm()
            
    else:
        form = QuestionForm()

    return render(request, 'question_list.html', {'form': form})
