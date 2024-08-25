from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionSet)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(AnswerDetail)