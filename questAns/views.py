from django.shortcuts import render # type: ignore
from django.views.generic import ListView, DetailView, CreateView # type: ignore
from .models import Question
# Create your views here.

class QuestListView(ListView):
    model = Question
    template_name = 'forumPages/forum.html'

class QuestDetailView(DetailView):
    model = Question
    template_name = 'forumPages/detail.html'

class QuestCreateView(CreateView):
    model = Question
    template_name = 'forumPages/ask_question.html'
    fields = '__all__'

