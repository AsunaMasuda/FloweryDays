from django.test import TestCase
from profiles.models import UserProfile
from django.contrib.auth.models import User


class TestUserProfile(TestCase):
    def test_userprofile(self):
        user = User(username='testuser')
        user.save()
        userprofile = UserProfile(user=user, default_email='default@test.com')
        self.assertEqual(str(userprofile), 'testuser, default@test.com')
