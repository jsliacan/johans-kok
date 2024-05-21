FROM python:3.9-slim

WORKDIR /johans-kok

ENV HOST=0.0.0.0

COPY app.py requirements.txt /johans-kok/
COPY templates/* /johans-kok/templates/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# use this below instead of ["flask", "run", "--host=${HOST}"] 
# because env vars aren't evaluated in the above :(
CMD ["bash", "-c", "flask run --host=${HOST}"]


FROM python:3.11

WORKDIR /johans-kok

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "app:app"]