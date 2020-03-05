from rest_framework import serializers
from .models import MCQquestion


class MCQquestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQquestion
        fields = [
            'id',
            'mainQuestion',
            'field',
            'optA',
            'optB',
            'optC',
            'optD',
        ]

    def create(self, validated_data):
        return MCQquestion.objects.create(**validated_data)
