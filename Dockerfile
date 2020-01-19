FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN pip install poetry
RUN poetry config settings.virtualenvs.create false
COPY poetry.lock pyproject.toml ./

# for poetry
RUN mkdir -p /app/app/
RUN touch /app/app/__init__.py


RUN poetry install -n


COPY ./app /app/app