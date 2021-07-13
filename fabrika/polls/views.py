from django.shortcuts import render, HttpResponse
from .models import Question, Choice, Poll
from .serializers import QuestionSerializer, ChoiceSerializer, PollSerializer
from .forms import ChoiceForm, MultipleChoiceForm, UserTextForm
from rest_framework import viewsets

class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

def polls_list(request):
    polls = Poll.objects.all()
    context = {'polls' : polls}
    return render(request, 'polls/polls_list.html', context)

def poll(request, id): 
    poll = Poll.objects.filter(id=id) 
    questions = Question.objects.filter(poll=id).prefetch_related('choice_set').all()
    context = {
        'poll' : poll,
        'questions' : questions,
    }
    return render(request, 'polls/poll.html', context)

def question(request, id):
    q = Question.objects.get(id=id)
    choices = q.choice_set.all()
    if q.question_type == 'Choice':
        form = ChoiceForm(choices=choices)
    elif q.question_type == 'MultipleChoice':
        form = MultipleChoiceForm(choices=choices)
    elif q.question_type == 'UserText':
        form = UserTextForm()
    context = {
        'question' : q,
        'form' : form
    }
    
    return render(request, 'polls/q.html', context=context)
