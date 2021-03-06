from django.test import TestCase
from api.tests.factories import UserFactory


class WorkflowTests(TestCase):
    def setUp(self):
        self.user = UserFactory(username="next_type")

    def test_username_validName_correctValue(self):
        self.assertEqual(
            self.user.username,
            "next_type"
        )
