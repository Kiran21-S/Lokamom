from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.views.generic import ListView, DetailView, CreateView, DeleteView # type: ignore
from .models import Question, Reply
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.urls import reverse_lazy # type: ignore
# Create your views here.

class QuestListView(ListView):
    model = Question
    template_name = 'forumPages/forum.html'
    def get_queryset(self):
        return Question.objects.all().order_by('-id')

class QuestDetailView(DetailView):
    model = Question
    template_name = 'forumPages/detail.html'

class QuestCreateView(CreateView):
    model = Question
    template_name = 'forumPages/ask_question.html'
    fields = '__all__'

import pytz # type: ignore 

@login_required
def ask_question(request):
    if request.method == 'POST':
        quest = request.POST.get('quest')

        # Get user's timezone from cookies, fallback to UTC
        user_timezone = request.COOKIES.get("user_timezone", "UTC")
        try:
            user_tz = pytz.timezone(user_timezone)
        except pytz.UnknownTimeZoneError:
            user_tz = pytz.UTC  # If invalid, default to UTC

        # Get current time in user's timezone
        local_time = timezone.now().astimezone(user_tz)
        local_date = timezone.now().astimezone(user_tz).date()

        if quest:
            question = Question(quest=quest, questioner=request.user, time=local_time, date = local_date)
            question.save()
            return redirect('forums')

    return render(request, "forumPages/ask_question.html")


def send_reply(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        answer = request.POST.get('reply')
        user_timezone = request.COOKIES.get("user_timezone", "UTC")
        try:
            user_tz = pytz.timezone(user_timezone)
        except pytz.UnknownTimeZoneError:
            user_tz = pytz.UTC

        local_time = timezone.now().astimezone(user_tz)
        local_date = timezone.now().astimezone(user_tz).date()
        if answer.strip():
            reply = Reply(answer=answer, answerer = request.user, question = question, time = local_time, date = local_date)
            reply.save()
            return redirect("question_detail", pk=pk)
    context = {'question': question}
    return render(request,"forumPages/detail.html", context)

class YourPostsView(ListView):
    model = Question
    template_name = 'profilePages/yourPosts.html'
    def get_queryset(self):
        return Question.objects.all().order_by('-id')

class QuestDeleteView(DeleteView):
    model = Question
    template_name = 'profilePages/deletePosts.html'  # Create this template
    success_url = reverse_lazy('yourPosts')
