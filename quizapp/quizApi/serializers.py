from rest_framework import serializers
from .models import MCQquestion, AllQuestion, TextQuestion, Hintquestion
from django.contrib.auth.models import User


class AllSerializer(serializers.ModelSerializer):
    creator = serializers.CharField()
    Answer_of = serializers.StringRelatedField(required=False) 
    Hints_of  = serializers.StringRelatedField(required=False)
    Option_of = serializers.StringRelatedField(required=False)
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
        # depth = 1

    def create(self, validated_data):
        user = User.objects.get(username=validated_data["creator"])
        validated_data["creator"] = user

        # print("\n\n\n\n {} \n\n\n".format(validated_data))

        return AllQuestion.objects.create(**validated_data)


class TextSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer()

    class Meta:
        model = TextQuestion
        fields = [
            'id',
            'answer',
            'questionInfo'
        ]
        depth = 1

    def create(self, validated_data):
        questionInfo = validated_data.pop("questionInfo")
        serializer = AllSerializer(data=questionInfo)
        if serializer.is_valid():
            question = serializer.save()
            validated_data["questionInfo"] = question
            return TextQuestion.objects.create(**validated_data)


class HintSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer()

    class Meta:
        model = Hintquestion
        fields = [
            'id',
            'noOfHints',
            'hintA', 'hintB', 'hintC', 'hintD',
            'hintE', 'hintF', 'hintG', 'hintH', 'hintI',
            'correctAnswer',
            'questionInfo'
        ]
        depth = 1

    def create(self, validated_data):
        questionInfo = validated_data.pop("questionInfo")
        serializer = AllSerializer(data=questionInfo)
        if serializer.is_valid():
            question = serializer.save()
            validated_data["questionInfo"] = question
            return Hintquestion.objects.create(**validated_data)


class MCQSerializer(serializers.ModelSerializer):
    questionInfo = AllSerializer()

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
        depth = 1

    def create(self, validated_data):
        # print("\n\nIn TextSserializer Create\n---------------------------\n {} \n\n\n".format(validated_data))
        questionInfo = validated_data.pop("questionInfo")
        serializer = AllSerializer(data=questionInfo)
        if serializer.is_valid():
            question = serializer.save()
            validated_data["questionInfo"] = question
            return MCQquestion.objects.create(**validated_data)


# class MCQSerializerAdd(serializers.ModelSerializer):
#     questionInfo = AllSerializer(read_only=True)

#     class Meta:
#         model = MCQquestion
#         fields = [
#             'id',
#             'optA',
#             'optB',
#             'optC',
#             'optD',
#             'corrOpt',
#             'questionInfo'
#         ]

#     def create(self, validated_data):
#         return MCQquestion.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MCQquestion.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']
