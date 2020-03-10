from rest_framework import serializers
from .models import MCQquestion, AllQuestion, TextQuestion, Hintquestion
from django.contrib.auth.models import User


class AllSerializer(serializers.ModelSerializer):
    creator = serializers.CharField()
    # Answer_of = serializers.StringRelatedField()
    # Hints_of = serializers.StringRelatedField()
    # Option_of = serializers.StringRelatedField()

    class Meta:
        model = AllQuestion
        fields = [
            'id',
            'questionText',
            'field',
            'questionType',
            'created',
            'creator',
            'Answer_of',
            'Hints_of',
            'Option_of',
        ]
        depth = 1

    def create(self, validated_data):
        user = User.objects.get(username=validated_data["creator"])
        validated_data["creator"] = user

        print("\n\n\n\n {} \n\n\n".format(validated_data))

        return AllQuestion.objects.create(**validated_data)


class TextSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer(read_only=True)

    class Meta:
        model = TextQuestion
        fields = [
            'id',
            'answer',
            'questionInfo'
        ]


# def ans_of(*args, **kwargs):
#     return TextSerializer()


# AllSerializer.get_Answer_of = ans_of


class HintSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer(read_only=True)

    class Meta:
        model = Hintquestion
        fields = [
            'id',
            'noOfHints',
            'hintA', 'hintB', 'hintC', 'hintD',
            'hintE', 'hintF', 'hintG', 'hintH', 'hintI'
            'correctAnswer',
            'questionInfo'
        ]


class MCQSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer(read_only=True)

    class Meta:
        model = MCQquestion
        fields = [
            'id',
            'optA',
            'optB',
            'optC',
            'optD',
            'corrOpt',
            'questionInfo'
        ]


class MCQSerializerAdd(serializers.ModelSerializer):
    questionInfo = AllSerializer(read_only=True)

    class Meta:
        model = MCQquestion
        fields = [
            'id',
            'optA',
            'optB',
            'optC',
            'optD',
            'corrOpt',
            'questionInfo'
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
