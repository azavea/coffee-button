import os
import json
import httpretty
import unittest

from functions.Slack.main import handle, ButtonClickType


class SlackTestCase(unittest.TestCase):
    """Test processing of IoT button states"""

    def setUp(self):
        self.slack_webhook_url = "https://hooks.slack.com/test"
        self.slack_channel = '#test'

        os.environ['COFFEE_BUTTON_SLACK_WEBHOOK_URL'] = self.slack_webhook_url
        os.environ['COFFEE_BUTTON_SLACK_CHANNEL'] = self.slack_channel

        httpretty.enable()
        httpretty.register_uri(httpretty.POST, self.slack_webhook_url)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_single_click_type(self):
        handle({'clickType': str(ButtonClickType.Single)}, None)
        self.assertTrue(httpretty.has_request())
        self.assertTrue("brewing" in json.loads(
            httpretty.last_request().body)['text'])

    def test_double_click_type(self):
        handle({'clickType': str(ButtonClickType.Double)}, None)
        self.assertTrue(httpretty.has_request())
        self.assertTrue("Jack-O-Lantern" in json.loads(
            httpretty.last_request().body)['text'])

    def test_long_click_type(self):
        handle({'clickType': str(ButtonClickType.Long)}, None)
        self.assertTrue(httpretty.has_request())
        self.assertTrue("ready" in json.loads(
            httpretty.last_request().body)['text'])
