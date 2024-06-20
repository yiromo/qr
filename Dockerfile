FROM python:3.9

WORKDIR /src

RUN apt-get update \
    && apt-get install -y \
       libzbar-dev \
       libmagickwand-dev 

COPY requirements.txt .
COPY ./src ./src


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/main.py"]