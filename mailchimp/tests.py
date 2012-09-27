import unittest
from api import MailChimp, MailChimpError

# Set this to your desired API key:
MAILCHIMP_API_TEST_KEY = ""


class TestMailChimp(unittest.TestCase):
    def setUp(self):
        self.api = MailChimp(MAILCHIMP_API_TEST_KEY)

    def test_ping(self):
        self.failUnlessEqual(self.api.ping(), u"Everything's Chimpy!")

    def test_blank_key_error(self):
        api = MailChimp("")
        self.failUnlessRaises(MailChimpError, api.ping)

    def test_invalid_key_error(self):
        api = MailChimp("invalid-us1")
        self.failUnlessRaises(MailChimpError, api.ping)

    def test_invalid_method_error(self):
        self.failUnlessRaises(MailChimpError, self.api.nonexistent_foo)

if __name__ == "__main__":
    unittest.main()
