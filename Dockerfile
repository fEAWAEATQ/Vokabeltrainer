FROM python:3.12-slim

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY nginx.conf /etc/nginx/conf.d/default.conf


RUN cp -r frontend/* /usr/share/nginx/html/


EXPOSE 80

CMD service nginx start && gunicorn -b 0.0.0.0:8000 backend.app:app
