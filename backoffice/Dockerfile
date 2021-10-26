FROM python:3.9.7-alpine
WORKDIR /src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN pip install -r requirements.txt