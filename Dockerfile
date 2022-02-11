FROM python:3.6-slim

RUN apt update -y \
    && apt install -y curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && $HOME/.poetry/bin/poetry config virtualenvs.create false

ADD poetry.lock pyproject.toml ./
RUN $HOME/.poetry/bin/poetry install \
    && $HOME/.poetry/bin/poetry run pyright --help  # Installs NPM requirements
