FROM python:3.12-slim

# Nginx installieren
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code kopieren
COPY backend ./backend
COPY frontend ./frontend
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Frontend nach nginx html
RUN cp -r frontend/* /usr/share/nginx/html/

# Nginx hört auf 10000 (Render)
EXPOSE 10000

# Start: Gunicorn im Hintergrund, Nginx im Vordergrund
CMD gunicorn backend.app:app --bind 0.0.0.0:8000 & nginx -g "daemon off;"
