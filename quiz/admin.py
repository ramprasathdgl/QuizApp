from django.contrib import admin
from quiz.models import Question, Choice, UserDetail

class ChoiceInline(admin.StackedInline):
    model = Choice
    extar = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['question_text']}),
                ('Correct  Answer', {'fields': ['answer_text'],
                'classes': ['collapse']}),
            ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserDetail)
