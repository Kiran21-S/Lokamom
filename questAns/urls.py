from django.urls import path # type: ignore
from .views import QuestListView, QuestCreateView, QuestDetailView

urlpatterns = [
    path('',QuestListView.as_view(), name = 'forums'),
    path('question/<int:pk>/', QuestDetailView.as_view(), name="question_detail"),
    path('question/new', QuestCreateView.as_view(), name='ask_question')
]
