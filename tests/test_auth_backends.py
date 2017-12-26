import json
from django.contrib.auth import authenticate
from django.core.management import call_command
from django.db.models import Q
from django.db import transaction
from django.test import TransactionTestCase
from django.utils import translation
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from starterkit.auth import *
from starterkit.utils import *


TEST_USER_FIRST_NAME = "Bart"
TEST_USER_LAST_MIKA = "Mika"
TEST_USER_EMAIL = "bart@overfiftyfive.com"
TEST_USER_USERNAME = "bart@overfiftyfive.com"
TEST_USER_PASSWORD = "123P@$$w0rd"


class TestBackends(TransactionTestCase):
    """
    Console:
    python manage.py test starterkit.tests.test_auth_backends
    """
    def setUp(self):
        translation.activate('en')  # Set English
        user = User.objects.create(
            first_name=TEST_USER_FIRST_NAME,
            last_name=TEST_USER_LAST_MIKA,
            email=TEST_USER_EMAIL,
            username=get_unique_username_from_email(TEST_USER_EMAIL),
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        user.set_password(TEST_USER_PASSWORD)
        user.save()
        super(TestBackends, self).setUp()

    def tearDown(self):
        users = User.objects.all()
        for user in users.all():
            user.delete()
        super(TestBackends, self).tearDown()

    def test_authentication_with_success(self):
        auth_user = authenticate(username=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)
        self.assertIsNotNone(auth_user)

    def test_authentication_with_failure(self):
        auth_user = authenticate(username=TEST_USER_EMAIL, password="Some-bad-password")
        self.assertIsNone(auth_user)

        # Bad username plus bad password.
        auth_user = authenticate(username="Some-bad-password", password="Some-bad-password")
        self.assertIsNone(auth_user)
