FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.2

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev

RUN apt install -y netcat
# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR app/
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:

ADD run_server.sh /run_server.sh
ADD run_queue.sh /run_queue.sh
RUN chmod a+x /run_server.sh /run_queue.sh
COPY . app/