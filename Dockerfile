FROM python:3.9

RUN apt-get update && apt-get upgrade -y

WORKDIR /app
COPY . /app

EXPOSE 80

COPY requirements.txt /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "django_training.wsgi"]
