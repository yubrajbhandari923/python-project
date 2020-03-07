from django.contrib import admin
from .models import MCQquestion, Hintquestion, AllQuestion, TextQuestion
# Register your models here.

admin.site.register(MCQquestion)
admin.site.register(Hintquestion)
admin.site.register(AllQuestion)
admin.site.register(TextQuestion)
