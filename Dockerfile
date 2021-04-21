# FROM python:3.8-slim
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./app /app/

# WORKDIR /app

# install python dependencies
# RUN pip install --upgrade pip
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . ./

# CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000