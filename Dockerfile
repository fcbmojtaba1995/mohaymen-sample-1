FROM python:3.9.6-buster

LABEL maintainer="mojtabaahmadi13740301@gmail.com"
LABEL version="1.0"

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /src/

CMD ["python", "main.py"]
