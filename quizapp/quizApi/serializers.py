from rest_framework import serializers
from .models import Project, QuestionSet, TextQuestion, Hintquestion, MCQquestion
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionSet
        fields = "__all__"


class TextSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username")

    class Meta:
        model = TextQuestion
        fields = "__all__"
        depth = 1


class HintSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username")

    class Meta:
        model = Hintquestion
        fields = "__all__"
        depth = 1


class MCQSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username")

    class Meta:
        model = MCQquestion
        fields = "__all__"
        depth = 1
