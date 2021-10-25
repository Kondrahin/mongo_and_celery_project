FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir poetry==1.1.6 && \
  poetry config virtualenvs.in-project true

RUN poetry install && rm -rf ~/.cache/pypoetry
