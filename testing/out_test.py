import unittest
from testing import enums


class TestEnum(unittest.TestCase):
    def test_enums_web_chat(self):
        self.assertEqual(enums.AccountApikeyPurpose.WEB_CHAT.value, "Web Chat")
        self.assertNotEqual(enums.AccountApikeyPurpose.WEB_CHAT.value, "web chat")

    @unittest.skip
    def test_enums_web_form(self):
        self.assertEqual(enums.AccountApikeyPurpose.WEB_FROM.value, "Web Fom")