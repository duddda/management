FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt base_requirements.txt /app/
RUN pip install -r base_requirements.txt
COPY . /app/


