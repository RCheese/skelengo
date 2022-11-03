FROM python:alpine AS base

FROM base AS builder
RUN apk update && apk add --no-cache --update curl libffi-dev musl-dev postgresql-dev zlib-dev pcre-dev build-base python3-dev

ENV POETRY_HOME /opt/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

ADD pyproject.toml .
ADD poetry.lock .
RUN poetry install --with dev,debug,speedups,test

FROM builder AS tester
COPY skelengo skelengo
ADD README.md .

FROM tester AS packager
RUN poetry build
RUN find / -iname "*.whl" -exec cp "{}" /tmp/ \;

FROM base AS pre_installer
RUN apk add libffi musl libstdc++ libgcc libpq zlib pcre libuv
COPY --from=packager /tmp /wheels

FROM pre_installer as installer
RUN pip install --no-index --find-links=/wheels skelengo[speedups]

FROM base AS executor
COPY --from=installer /usr /usr

FROM pre_installer AS dev_installer
RUN pip install --no-index --find-links=/wheels skelengo[test,dev,debug,speedups]

FROM base AS dev_executor
COPY --from=dev_installer /usr /usr
