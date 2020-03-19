import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse


from quizApi.models import Hintquestion , AllQuestion
from quizApi.serializers import HintSerializer
from django.contrib.auth.models import User
client = APIClient()

# ----------------------------------------------------------------------------------------------------
                                    #  """ TEST FOR /questions/hints """
# ----------------------------------------------------------------------------------------------------
class HintQuestionTest(TestCase):
    url = "get_post_hintquestions"

    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")
        question = AllQuestion.objects.create(
            questionText="Who is the Father of Science?", field="sci", questionType="txt", creator=user)
        Hintquestion.objects.create(
            correctAnswer="Albert Einstine",noOfHints=2, 
            hintA="He gave Photo Electric effect.", hintB="He won Nobel Prize in 1927." ,questionInfo=question)
        client.force_authenticate(user=user)
        self.valid_payload = {
           "correctAnswer":"Albert Einstine","noOfHints":2, 
            "hintA":"He gave Photo Electric effect.", "hintB":"He won Nobel Prize in 1927." ,
           "questionInfo" : {
                "questionText": "Who is the father of Biology?",
                "questionType": "MCQ",
                "field": "sci"
            }

        }
        self.invalid_payload = {
            "answer" : "Aristotle",
            "questionInfo" : {
            "questionText": "Who is the father of Biology?",
            "questionType": "Multipple",
            "field": "science"}
        }

    def test_get_hintQuestion(self):
        response = client.get(
            reverse(self.url)
            
        )
        questions =  Hintquestion.objects.all()
        serializer = HintSerializer(questions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_hintQuestion(self):
        response = client.post(
            reverse(self.url),
            data = json.dumps(self.valid_payload),
            content_type= "application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_hintQuestion(self):
        response = client.post(
            reverse(self.url),
            data = json.dumps(self.invalid_payload),
            content_type= "application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_unauth_hintquestion(self):
        client.force_authenticate(user=None)
        response = client.post(
            reverse(self.url),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class HintQuestionOneTest(TestCase):
    url = "get_one_hintquestions"

    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")
        question = AllQuestion.objects.create(
            questionText="Who is the Father of Science?", field="sci", questionType="txt", creator=user)
        Hintquestion.objects.create(
            correctAnswer="Albert Einstine",noOfHints=2, 
            hintA="He gave Photo Electric effect.", hintB="He won Nobel Prize in 1927.", questionInfo=question)
        client.force_authenticate(user=user)

    def test_retrive_textquestion(self):
        response = client.get(reverse(self.url, args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_hintquestion(self):
        response = client.delete(reverse(self.url, args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_delete_hintquestion(self):
        response = client.delete(reverse(self.url, args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)