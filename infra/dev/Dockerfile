FROM python:3.10.4
ARG USER_ID
ARG GROUP_ID
RUN addgroup --system --gid $GROUP_ID webuser
RUN adduser --system --uid $USER_ID --gid $GROUP_ID webuser
USER webuser
ENV PYTHONFAULTHANDLER=true \
    PYTHONUNBUFFERED=true \
    PIP_NO_CACHE_DIR=true \
    PYTHONDONTWRITEBYTECODE=true \
    POETRY_VERSION=1.1.13 \
    PATH="${PATH}:/home/webuser/.local/bin" \
    POETRY_VIRTUALENVS_CREATE=false
WORKDIR /code
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks
