FROM python:3.10.4
ENV PYTHONFAULTHANDLER=true \
    PYTHONUNBUFFERED=true \
    PIP_NO_CACHE_DIR=true \
    PYTHONDONTWRITEBYTECODE=true
WORKDIR /code
COPY infra/prod/requirements.txt .
RUN pip install -r requirements.txt
