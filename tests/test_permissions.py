from mock import patch, MagicMock
from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User, Group
from starterkit.drf.permissions import *
from starterkit.utils import *


TEST_USER_FIRST_NAME = "Bart"
TEST_USER_LAST_MIKA = "Mika"
TEST_USER_EMAIL = "bart@mikasoftware.com"


class TestPermissions(TestCase):
    """
    Console:
    python manage.py test starterkit.tests.test_permissions
    """

    def setUp(self):
        super(TestPermissions, self).setUp()

        # Setup our users.
        self.suspended_user = User.objects.create(
            first_name=TEST_USER_FIRST_NAME,
            last_name=TEST_USER_LAST_MIKA,
            email='bart+suspended@mikasoftware.com',
            username=get_unique_username_from_email('bart+suspended@mikasoftware.com'),
            is_active=False,
            is_superuser=True,
            is_staff=True
        )
        self.active_user = User.objects.create(
            first_name=TEST_USER_FIRST_NAME,
            last_name=TEST_USER_LAST_MIKA,
            email='bart@mikasoftware.com',
            username=get_unique_username_from_email('bart@mikasoftware.com'),
            is_active=True,
            is_superuser=True,
            is_staff=True
        )

        # Setup our view mockups.
        self.anon_request = MagicMock(user=AnonymousUser())
        self.suspended_request = MagicMock(user=self.suspended_user)
        self.active_request = MagicMock(user=self.active_user)
        self.view = MagicMock()

    def tearDown(self):
        User.objects.all().delete()
        del self.anon_request
        del self.suspended_request
        del self.active_request
        del self.view
        super(TestPermissions, self).tearDown()

    def test_is_auth_and_is_active_permission(self):
        # Variable is just a sample object.
        mock_object = MagicMock()

        # Variable is our permission class.
        permission = IsAuthenticatedAndIsActivePermission()

        # VIEW BASED.

        # CASE 1 - Anon user.
        self.assertFalse(
            permission.has_permission(self.anon_request, self.view)
        )

        # CASE 2 - Suspended user.
        self.assertFalse(
            permission.has_permission(self.suspended_request, self.view)
        )

        # CASE 3 - Active user.
        self.assertTrue(
            permission.has_permission(self.active_request, self.view)
        )

        # OBJECT BASED.

        # CASE 1 - Anon user.
        self.assertFalse(
            permission.has_object_permission(self.anon_request, self.view, mock_object)
        )

        # CASE 2 - Suspended user.
        self.assertFalse(
            permission.has_object_permission(self.suspended_request, self.view, mock_object)
        )

        # CASE 3 - Active user.
        self.assertTrue(
            permission.has_object_permission(self.active_request, self.view, mock_object)
        )

# How to unit test permissions in django-rest-framework?
# https://stackoverflow.com/a/37172220
