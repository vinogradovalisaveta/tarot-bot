FROM python:3.10-alpine

WORKDIR /tarot_bot

RUN pip install --no-cache-dir pip && pip install poetry --no-cache-dir;

COPY pyproject.toml poetry.lock /tarot_bot/

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi --no-cache;

COPY . .

CMD ["python3 main.py"]