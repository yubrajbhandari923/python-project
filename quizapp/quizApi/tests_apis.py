import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse


from .models import AllQuestion
from .serializers import AllSerializer
from django.contrib.auth.models import User
client = APIClient()


class GetAllQuestionsTest(TestCase):
    """ Test module for GET all Questions API """

    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")
        AllQuestion.objects.create(
            questionText="Who is the Father of Science?", field="sci", questionType="txt", creator=user)
        AllQuestion.objects.create(
            questionText="Who is the Father of Computer?", field="sci", questionType="hin", creator=user)
        AllQuestion.objects.create(
            questionText="Who is the Father of Zoology?", field="sci", questionType="MCQ", creator=user)
        AllQuestion.objects.create(
            questionText="Who is the Father of Botany?", field="sci", questionType="txt", creator=user)

    def test_get_all_allQuestion(self):
        # get API response
        response = client.get(
            reverse('get_post_allquestions'))
        # get data from db
        questions = AllQuestion.objects.all()
        serializer = AllSerializer(questions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostAllquestionTest(TestCase):
    """ Test module for cheacking post functionality of Allquestion"""
    # client.credentials(HTTP_AUTHORIZATION='Basic ' + 'yubraj1:Password098')

    def setUp(self):
        user = User.objects.create_user(
            username="yubraj1", password="Password098")
        client.force_authenticate(user=user)
        self.valid_payload = {
            'questionText': 'Who is the father of Biology?',
            'questionType': 'MCQ',
            'field': 'sci'
        }
        self.invalid_payload = {
            'questionText': 'Who is the father of Biology?',
            'questionType': 'Multipple',
            'field': 'science'
        }

    def test_create_valid_Addquestion(self):
        response = client.post(
            reverse('get_post_allquestions'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            # headers=auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_Addquestion(self):
        response = client.post(
            reverse('get_post_allquestions'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_unauth_Addquestion(self):
        client.force_authenticate(user=None)
        response = client.post(
            reverse('get_post_allquestions'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
