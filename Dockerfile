FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "timeout 3600 gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 2 app:app"]
