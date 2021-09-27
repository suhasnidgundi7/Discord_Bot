from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Question(models.Model):

    LEVEL = (
        (0, _('ANY')),
        (1, _('BEGINNER')),
        (2, _('INTERMEDIATE')),
        (3, _('ADVANCED')),
        (4, _('EXPERT')),
    )

    title = models.CharField(_("title"), max_length=255)
    points = models.SmallIntegerField(_("points"))
    difficulty = models.IntegerField(_("Difficulty"), choices=LEVEL, default=0)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name=_("Question"), on_delete=models.CASCADE)
    answer = models.CharField(_("Answer"), max_length=255)
    is_correct = models.BooleanField(_("Correct Answer"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.answer