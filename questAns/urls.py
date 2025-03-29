from django.urls import path # type: ignore
from .views import QuestListView, YourPostsView
from . import views
urlpatterns = [
    path('',QuestListView.as_view(), name = 'forums'),
    path('question/<int:pk>/', views.send_reply, name="question_detail"),
    path('question/new', views.ask_question, name='ask_question'),
    path('your-posts', YourPostsView.as_view(), name="yourPosts" ),
    path('your-profile', views.showProfile, name="yourProfile")
]
