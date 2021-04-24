FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./

CMD uvicorn app.main:app --reload --host 0.0.0.0