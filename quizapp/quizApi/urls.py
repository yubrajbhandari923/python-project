from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionList, QuestionDetail, UserList, UserDetail

urlpatterns = [
    path('q', QuestionList.as_view(), name='get_post_allquestions'),
    path('q/<int:pk>', QuestionDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
