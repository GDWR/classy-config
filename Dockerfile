FROM python:3.6

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
  && $HOME/.poetry/bin/poetry config virtualenvs.create false

ADD poetry.lock pyproject.toml ./
RUN $HOME/.poetry/bin/poetry install
