build:
	docker build -t coffee-button:slack .

deploy: build
	@docker run --rm \
		-e AWS_REGION="us-east-1" \
		-e AWS_ACCESS_KEY_ID="$(AWS_ACCESS_KEY_ID)" \
		-e AWS_SECRET_ACCESS_KEY="$(AWS_SECRET_ACCESS_KEY)" \
	 	coffee-button:slack apex deploy Slack \
			-a "$(COFFEE_BUTTON_FUNCTION_ALIAS)" \
			-s COFFEE_BUTTON_SLACK_WEBHOOK_URL="$(COFFEE_BUTTON_SLACK_WEBHOOK_URL)" \
			-s COFFEE_BUTTON_SLACK_CHANNEL="$(COFFEE_BUTTON_SLACK_CHANNEL)"

test: build
	docker run --rm coffee-button:slack py.test

.PHONY: build deploy test
