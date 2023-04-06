from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'food/question_list.html', context)

def result(request):
    return render(request,'food/result.html')

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'food/question_detail.html', context)