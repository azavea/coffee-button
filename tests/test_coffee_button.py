import os
import requests_mock
import unittest


from functions.Slack.main import handle, ButtonClickType


class SlackTestCase(unittest.TestCase):
    """Test that Candidate parsing works correctly"""

    @classmethod
    def setUpClass(self):
        self.slack_webhook_url = "https://hooks.slack.com/test"
        self.slack_channel = '#test'
        self.mock = requests_mock.Mocker()
        self.mock.post(self.slack_webhook_url)

        os.environ['COFFEE_BUTTON_SLACK_WEBHOOK_URL'] = self.slack_webhook_url
        os.environ['COFFEE_BUTTON_SLACK_CHANNEL'] = self.slack_channel

    def test_single_click_type(self):
        handle({'clickType': str(ButtonClickType.Single)}, None)
        self.assertEquals(self.mock.call_count, 1)

    def test_single_click_type(self):
        handle({'clickType': str(ButtonClickType.Double)}, None)
        self.assertEquals(self.mock.call_count, 0)

    def test_single_click_type(self):
        handle({'clickType': str(ButtonClickType.Long)}, None)
        self.assertEquals(self.mock.call_count, 0)
