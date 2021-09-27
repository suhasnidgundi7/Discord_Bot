from django.contrib import admin
from . import models

# Register your models here.
class AnswerInLine(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer',
        'is_correct',
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
        'difficulty'
    ]

    list_display = [
        'title',
        'updated_at'
    ]

    inlines = [
        AnswerInLine
    ]