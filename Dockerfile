FROM python:3.7

WORKDIR /app
ADD /app/app.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--port", "80", '--host=', '0.0.0.0']
