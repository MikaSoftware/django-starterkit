from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.password_validation import get_password_validators
from django.test import SimpleTestCase
from django.urls import reverse
from django.test import override_settings
from starterkit.password_validation import *


UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG = [{
    'NAME': 'starterkit.password_validation.UppercaseCharacterPasswortValidator',
    'OPTIONS': {
       'min_occurrence': 1,
    }
}]

UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_MULTIPLTE_CHARS_CONFIG = [{
    'NAME': 'starterkit.password_validation.UppercaseCharacterPasswortValidator',
    'OPTIONS': {
       'min_occurrence': 5,
    }
}]

SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG = [{
    'NAME': 'starterkit.password_validation.SpecialCharacterPasswortValidator',
    'OPTIONS': {
       'min_occurrence': 1,
    }
}]

SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_MULTIPLTE_CHARS_CONFIG = [{
    'NAME': 'starterkit.password_validation.SpecialCharacterPasswortValidator',
    'OPTIONS': {
       'min_occurrence': 5,
    }
}]


class TestPasswordValidation(SimpleTestCase):
    """
    Console:
    python manage.py test starterkit.tests.test_password_validation
    """

    def setUp(self):
        super(TestPasswordValidation, self).setUp()

    def tearDown(self):
        del self.client
        super(TestPasswordValidation, self).tearDown()

    def test_uppercase_password_valdator_get_help_text(self):
        validators = get_password_validators(UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
        for validator in validators:
            self.assertIn("Validator enforces that the password contain uppercase character(s).", validator.get_help_text())

    @override_settings(AUTH_PASSWORD_VALIDATORS=UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
    def test_uppercase_password_valdator_with_single_character_and_failure(self):
        try:
            validate_password('123password')
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIn("Password must contain at least a single uppercase character.", str(e))

    @override_settings(AUTH_PASSWORD_VALIDATORS=UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_MULTIPLTE_CHARS_CONFIG)
    def test_uppercase_password_valdator_with_multiple_characters_and_failure(self):
        try:
            validate_password('123Password')
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIn("Password must contain as least 5 uppercase characters", str(e))

    @override_settings(AUTH_PASSWORD_VALIDATORS=UPPERCASE_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
    def test_uppercase_password_valdator_with_success(self):
        validate_password('123Password')
        self.assertTrue(True)

    def test_special_password_valdator_get_help_text(self):
        validators = get_password_validators(SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
        for validator in validators:
            self.assertIn("Validator enforces that the password character contains special character(s)", validator.get_help_text())

    @override_settings(AUTH_PASSWORD_VALIDATORS=SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
    def test_special_password_valdator_with_single_character_and_failure(self):
        try:
            validate_password('123password')
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIn("Password must contain at least a single special character.", str(e))

    @override_settings(AUTH_PASSWORD_VALIDATORS=SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_MULTIPLTE_CHARS_CONFIG)
    def test_special_password_valdator_with_multiple_characters_and_failure(self):
        try:
            validate_password('123Password')
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIn("Password must contain as least 5 special characters", str(e))

    @override_settings(AUTH_PASSWORD_VALIDATORS=SPECIAL_CHARACTER_PASSWORD_VALIDATOR_WITH_SINGLE_CHARS_CONFIG)
    def test_special_password_valdator_with_success(self):
        validate_password('123password!')
        self.assertTrue(True)
