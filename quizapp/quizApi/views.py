from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly

from .models import AllQuestion, TextQuestion, Hintquestion, MCQquestion
from .serializers import AllSerializer, TextSerializer, HintSerializer, MCQSerializer, UserSerializer



class QuestionList(ModelViewSet):
    """
        List all questions or create new
    """
    queryset = AllQuestion.objects.all()
    serializer_class = AllSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):

        # print("\n\n\n {} \n\n\n {} \n\n\n {} :::: {} ".format(
        #     request.headers, request.body, request.user, request.data))
        #
        request.data["creator"] = request.user.username
        print(request.data)
        serializer = AllSerializer(data=request.data)
#
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, format=None):
        question = get_object_or_404(AllQuestion, pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)

#


# class QuestionDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
#     ]

#     def get_object_or_404(self, pk):
#         try:
#             return MCQquestion.objects.get(pk=pk)
#         except MCQquestion.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         question = self.get_object_or_404(pk)
#         serializer = MCQSerializer(question)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         question = self.get_object_or_404(pk)
#         serializer = MCQSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         question = self.get_object_or_404(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class TextViewset(ModelViewSet):
    queryset = TextQuestion.objects.all()
    serializer_class = TextSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request):
        request.data["questionInfo"]["creator"] = request.user.username
        # print("\nIn Viewset\n-----------------------\n{}\n\n\n".format(request.data))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, format=None):
        question = get_object_or_404(TextQuestion, pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)

    def destory(self, request, pk=None, format=None):
        question = get_object_or_404(TextQuestion, pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None, format=None):
        question = get_object_or_404(TextQuestion, pk=pk)
        serializer = self.serializer_class(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        



class HintViewset(ModelViewSet):
    queryset = Hintquestion.objects.all()
    serializer_class = HintSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request):
        request.data["questionInfo"]["creator"] = request.user.username
        # print("\nIn Viewset\n-----------------------\n{}\n\n\n".format(request.data))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, format=None):
        question = get_object_or_404(Hintquestion, pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)

    def destory(self, request, pk=None, format=None):
        question = get_object_or_404(Hintquestion, pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None, format=None):
        question = get_object_or_404(Hintquestion, pk=pk)
        serializer = self.serializer_class(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MCQViewset(ModelViewSet):
    queryset = MCQquestion.objects.all()
    serializer_class = MCQSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request):
        request.data["questionInfo"]["creator"] = request.user.username
        # print("\nIn Viewset\n-----------------------\n{}\n\n\n".format(request.data))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, format=None):
        question = get_object_or_404(MCQquestion, pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)

    def destory(self, request, pk=None, format=None):
        question = get_object_or_404(MCQquestion,pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None, format=None):
        question = get_object_or_404(MCQquestion, pk=pk)
        serializer = self.serializer_class(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)