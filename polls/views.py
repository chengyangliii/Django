from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.


def index(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'polls/index.html', context)


#def index(request):
#    return HttpResponse("Hello World")


def detail(request, question_id):
    return HttpResponse("You're looking at question"+question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question"+question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question"+question_id)