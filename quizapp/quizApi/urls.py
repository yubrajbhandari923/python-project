from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TextViewset, HintViewset, MCQViewset, ProjectViewSet, SetsViewSet

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),

    path('project/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='get_post_projects'),
    path('project/<int:pk>',
         ProjectViewSet.as_view({
             'get': 'retrieve',
             'delete': 'destroy',
             'patch': 'partial_update'}), name='get_one_projects'),

    path('sets/', SetsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='get_post_projects'),
    path('sets/<int:pk>',
         SetsViewSet.as_view({
             'get': 'retrieve',
             'delete': 'destroy',
             'patch': 'partial_update'}), name='get_one_projects'),
    path('project/<int:pk>/sets/', SetsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='get_post_projects'),
    path('project/<int:project-pk>/sets/<int:set-pk>', SetsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='get_post_projects'),




    path('text/',
         TextViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_textquestions'),
    path('text/<int:pk>',
         TextViewset.as_view({
             'get': 'retrieve',
             'delete': 'destroy',
             'patch': 'partial_update'}), name='get_one_textquestions'),

    path('hint/',
         HintViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_hintquestions'),
    path('hint/<int:pk>',
         HintViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), name='get_one_hintquestions'),

    path('mcq/',
         MCQViewset.as_view({'get': 'list', 'post': 'create'}), name='get_post_mcqquestions'),
    path('mcq/<int:pk>',
         MCQViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), name='get_one_mcqquestions'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
