from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionList, QuestionDetail

urlpatterns = [
    path('q', QuestionList.as_view()),
    path('q/<int:pk>', QuestionDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
