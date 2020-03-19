from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionList, TextViewset, HintViewset, MCQViewset

urlpatterns = [

    #     path('users/', UserList.as_view()),
    #     path('users/<int:pk>/', UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),

    path('questions', QuestionList.as_view(
        {'get': 'list', 'post': 'create'}), name='get_post_allquestions'),
    path('questions/<int:pk>',
         QuestionList.as_view({'get': 'retrieve'}, name='get_one_allquestions')),

    path('questions/text',
         TextViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_textquestions'),
    path('questions/text/<int:pk>',
         TextViewset.as_view({
             'get': 'retrieve',
             'delete': 'destroy',
             'patch': 'partial_update'}), name='get_one_textquestions'),

    path('questions/hint',
         HintViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_hintquestions'),
    path('questions/hint/<int:pk>',
         HintViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), name='get_one_hintquestions'),

    path('questions/mcq',
         MCQViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_mcqquestions'),
    path('questions/mcq/<int:pk>',
         MCQViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), name='get_one_mcqquestions'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
