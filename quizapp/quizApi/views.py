from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from .permissions import IsOwnerOrReadOnly

from .models import MCQquestion
from .serializers import MCQquestionSerializer, UserSerializer
# Create your views here.


class QuestionList(APIView):
    """
        List all questions or create new
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print("\n\n\n ********************************** Im Perform Create ****** \n\n\n")
        return serializer.save(creator=self.request.user)

    def get(self, request, format=None):
        question = MCQquestion.objects.all()
        serializer = MCQquestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("\n\n\n {} \n\n\n {} \n\n\n {} :::: {} ".format(
            request.headers, request.body, request.user, request.data))
        serializer = MCQquestionSerializer(data=request.data)
        # print("hello")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return MCQquestion.objects.get(pk=pk)
        except MCQquestion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = MCQquestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = MCQquestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET', 'POST'])
# def MCQquestion_list(request, format=None):
#     """
#         List all questions or create new
#     """
#     if request.method == 'GET':
#         question = MCQquestion.objects.all()
#         serializer = MCQquestionSerializer(question, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MCQquestionSerializer(question, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def MCQquestion_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         question = MCQquestion.objects.get(pk=pk)
#     except question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MCQquestionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = Serializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# def MCQquestion_list(request):
#     """
#     List all code questions, or create a new snippet.
#     """
#     if request.method == 'GET':
#         MCQquestions = MCQquestion.objects.all()
#         serializer = MCQquestionSerializer(MCQquestions, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':

#         print("\n\n\n\n")
#         print("\n\n\n\n")
#         print(request.headers)
#         print("\n\n\n\n")
#         print(request.body)
#         print("\n\n\n\n")
#         print("\n\n\n\n")
#         data = JSONParser().parse(request)
#         print("\n\n\n\n")
#         print("request got :", data)
#         print("\n\n\n\n")
#         serializer = MCQquestionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def MCQquestion_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         question = MCQquestion.objects.get(pk=pk)
#     except question.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = MCQquestionSerializer(question)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MCQquestionSerializer(question, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         question.delete()
#         return HttpResponse(status=204)
