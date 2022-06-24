FROM python:3.10

COPY ./app .

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.1.13 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

RUN apt-get update && apt-get upgrade -y \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    # Cleaning cache
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./app ./poetry.lock ./pyproject.toml ./

RUN poetry version \
    # Install deps:
    && poetry install \
    && rm -rf "$POETRY_CACHE_DIR"

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]

