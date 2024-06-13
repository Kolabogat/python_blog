FROM python:3.10

RUN apt update -y && apt upgrade -y
RUN python -m pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]