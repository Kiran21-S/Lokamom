from django.contrib import admin # type: ignore
from .models import Question, Reply
# Register your models here.

class ReplyInline(admin.StackedInline): # new
    model = Reply
class QuestionAdmin(admin.ModelAdmin): # new
    inlines = [
        ReplyInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Reply)
