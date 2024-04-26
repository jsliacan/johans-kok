FROM python:3.9-slim

WORKDIR /johans-kok

COPY .env app.py requirements.txt /johans-kok/
COPY templates/* /johans-kok/templates/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
