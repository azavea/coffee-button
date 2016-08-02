# coffee-button

[![Build Status](https://travis-ci.org/azavea/coffee-button.svg?branch=develop)](https://travis-ci.org/azavea/coffee-button)
[![Apache V2 License](http://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/azavea/coffee-button/blob/develop/LICENSE)

An Amazon Lambda function that publishes messages to a configured Slack channel when an Amazon IoT button is pressed.

## Table of Contents

* [Configuration](#configuration)
* [Testing](#testing)
* [Deployment](#deployment)

## Configuration

The following environment variables can be used to dictate which Slack webhook URL and channel are used:

- `COFFEE_BUTTON_SLACK_WEBHOOK_URL`: Slack webhook URL
- `COFFEE_BUTTON_SLACK_CHANNEL`: Slack channel to send messages to
- `COFFEE_BUTTON_FUNCTION_ALIAS`: When deploying, the alias associated with the Lambda function

## Testing

Function testing occurs within a Docker container and is driven by `make`:

```bash
$ make test
```

## Deployment

Function deployment occurs automatically via Travis CI. If you choose to execute deployments manually, run through the following steps:

```bash
$ export COFFEE_BUTTON_SLACK_WEBHOOK_URL="https://hooks.slack.com/..."
$ export COFFEE_BUTTON_SLACK_CHANNEL="#general"
$ export COFFEE_BUTTON_FUNCTION_ALIAS="staging"
$ export AWS_SECRET_ACCESS_KEY="..."
$ export AWS_ACCESS_KEY_ID="..."
$ make deploy
```

This deployment process makes use of `make` and [Apex](http://apex.run) to publish the function to Amazon Lambda.
