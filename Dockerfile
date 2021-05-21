FROM python:latest

RUN mkdir /build
WORKDIR /build

COPY ./containerapp/ /build

COPY containerapp/requirements.txt /build

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
