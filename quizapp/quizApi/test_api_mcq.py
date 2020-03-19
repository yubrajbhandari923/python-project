import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse


from quizApi.models import MCQquestion, AllQuestion
from quizApi.serializers import MCQSerializer
from django.contrib.auth.models import User
client = APIClient()

# ----------------------------------------------------------------------------------------------------
                                    #  """ TEST FOR /questions/mcq """
# ----------------------------------------------------------------------------------------------------
class MCQQuestionTest(TestCase):
    url = "get_post_mcqquestions"
    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")
        question = AllQuestion.objects.create(
            questionText="Who is the Father of Science?", field="sci", questionType="mcq", creator=user)
        MCQquestion.objects.create(
            optB="Albert Einstine", questionInfo=question,
            optA="Newton", optC="Plank", optD="Tesla", corrOpt="B")
        client.force_authenticate(user=user)
        self.valid_payload = {
            "optB":"Albert Einstine",
            "optA":"Newton", "optC":"Plank",
            "optD":"Tesla", "corrOpt":"B",
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

    def test_get_mcqQuestion(self):
        response = client.get(
            reverse(self.url)
            
        )
        questions =  MCQquestion.objects.all()
        serializer = MCQSerializer(questions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_mcqQuestion(self):
        response = client.post(
            reverse(self.url),
            data = json.dumps(self.valid_payload),
            content_type= "application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_mcqQuestion(self):
        response = client.post(
            reverse(self.url),
            data = json.dumps(self.invalid_payload),
            content_type= "application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_unauth_mcqquestion(self):
        client.force_authenticate(user=None)
        response = client.post(
            reverse(self.url),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MCQQuestionOneTest(TestCase):
    url = "get_one_mcqquestions"

    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")
        question = AllQuestion.objects.create(
            questionText="Who is the Father of Science?", field="sci", questionType="txt", creator=user)
        MCQquestion.objects.create(
            optB="Albert Einstine", questionInfo=question,
            optA="Newton", optC="Plank", optD="Tesla", corrOpt="B")
        client.force_authenticate(user=user)

        
    def test_retrive_mcqquestion(self):
        response = client.get(reverse(self.url, args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_mcqquestion(self):
        response = client.delete(reverse(self.url, args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_delete_mcqquestion(self):
        response = client.delete(reverse(self.url, args=[10]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_mcqquestion(self):
        payload = {
            'questionText' : 'who gave photoelectric effect?'
        }
        response = client.patch(
            reverse(self.url, args=[1]),
            data=json.dumps(payload), 
            content_type="application/json")
        question = MCQquestion.objects.get(pk=1)
        serializer = MCQSerializer(question)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data, serializer.data)