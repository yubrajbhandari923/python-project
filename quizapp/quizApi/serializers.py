from rest_framework import serializers
from .models import MCQquestion
from django.contrib.auth.models import User


class MCQquestionSerializer(serializers.ModelSerializer):

    class Meta:
        creator = serializers.ReadOnlyField(source='creator.username')
        model = MCQquestion
        fields = [
            'id',
            'mainQuestion',
            'field',
            'optA',
            'optB',
            'optC',
            'optD',
            'creator'
        ]

    def create(self, validated_data):
        return MCQquestion.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MCQquestion.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']
