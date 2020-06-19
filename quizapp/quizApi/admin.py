from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(QuestionSet)
admin.site.register(MCQquestion)
admin.site.register(Hintquestion)
admin.site.register(TextQuestion)
