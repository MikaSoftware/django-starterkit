from django.core.management import call_command
from django.conf import settings
from django.test import SimpleTestCase
from django.urls import reverse
from starterkit.utils import *


class TestUtils(SimpleTestCase):
    """
    Console:
    python manage.py test starterkit.tests.test_utils
    """

    def setUp(self):
        super(TestUtils, self).setUp()

    def tearDown(self):
        del self.client
        super(TestUtils, self).tearDown()

    def test_inc_range(self):
        max_i = 1
        arr = inc_range(1, 3)
        for i in arr:
            if i >= max_i:
                max_i = i
        self.assertEqual(max_i, 3)

    def test_get_random_string(self):
        value = get_random_string()
        self.assertIsNotNone(value)

    def test_generate_hash(self):
        value = "bart@overfiftyfive.com"
        hashed_value = generate_hash(value)
        self.assertIsNotNone(hashed_value)

    def test_generate_multiple_hashes(self):
        salt1 = generate_hash()
        self.assertIsNotNone(salt1)
        salt2 = generate_hash()
        self.assertIsNotNone(salt2)
        self.assertNotEqual(salt1, salt2)
        salt3 = generate_hash()
        self.assertIsNotNone(salt3)
        self.assertNotEqual(salt1, salt3)
        self.assertNotEqual(salt2, salt3)

    def test_get_unique_username_from_email(self):
        email_value = "bart@overfiftyfive.com"
        hashed_email_value = get_unique_username_from_email(email_value)

        # Ensure something was returned.
        self.assertIsNotNone(hashed_email_value)

        # Validate the 'User' fields "username" length restriction is enforced.
        self.assertTrue(len(hashed_email_value) <= 30)

    def test_int_or_none(self):
        value = int_or_none("LALALALA")
        self.assertIsNone(value)
        value = int_or_none("123")
        self.assertIsNotNone(value)
        self.assertEqual(value, 123)

    def test_float_or_none(self):
        value = float_or_none("LALALALA")
        self.assertIsNone(value)
        value = float_or_none("123.321")
        self.assertIsNotNone(value)
        self.assertEqual(value, 123.321)
