from django.test import TestCase
from api.tests.factories import UserFactory


class WorkflowTests(TestCase):
    def setUp(self):
        self.user1 = UserFactory(username="next_type")
        self.user2 = UserFactory(username="hoge_user")

    def test_username_validName_correctValue(self):
        self.assertEqual(
            self.user1.username,
            "next_type"
        )

    def test_username_validName_correctValue2(self):
        self.assertEqual(
            self.user2.username,
            "hoge_user"
        )
