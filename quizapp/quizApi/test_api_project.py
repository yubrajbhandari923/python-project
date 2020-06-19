from rest_framework.test import APIClient
from django.test import TestCase


from .models import Project
from .serializers import ProjectSerializer
from django.contrib.auth.models import User

client = APIClient()


# ----------------------------------------------------------------------------------------------------
                                #  """ TEST FOR /projects/ """
# ----------------------------------------------------------------------------------------------------

class ProjectsAPITest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="testUser", password="Password098")

        Project.objects.create(
            projectName ="TestProject",
            projectCreator=user
        )

        self.valid_payload = {
            'projectName' = 'TestProject'
            
        } 
