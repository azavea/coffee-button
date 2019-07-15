FROM python:2.7-alpine

WORKDIR /usr/src

RUN \
      apk add --no-cache ca-certificates \
      && apk add --no-cache --virtual .build-deps \
          curl \
      && pip install --no-cache \
          pytest \
          pytest-flake8 \
          httpretty \
          pytz \
          urllib3 \
          chardet \
          certifi \
          idna \
      && curl -s "https://raw.githubusercontent.com/apex/apex/master/install.sh" | sh \
      && apk del .build-deps

COPY . /usr/src

RUN \
      pip install --no-cache -t functions/Slack \
          enum34 \
          requests \
          pytz
