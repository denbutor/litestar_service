##FROM python:3.12-slim
##WORKDIR /app
##COPY requirements.txt ./
##RUN pip install --no-cache-dir -r requirements.txt
##COPY . /app
##ENV PYTHONUNBUFFERED=1
##CMD ["granian", "run", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
#
## 🐍 Базовий образ
#FROM python:3.12-slim
#
## 📂 Робоча директорія
#WORKDIR /app
#
## 🔧 Встановлюємо залежності системи (для psycopg2, rust тощо)
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libpq-dev \
#    && rm -rf /var/lib/apt/lists/*
#
## 📦 Копіюємо залежності
#COPY requirements.txt .
#
## 🚀 Встановлюємо Python-залежності
#RUN pip install --no-cache-dir --upgrade pip \
#    && pip install --no-cache-dir -r requirements.txt
#
## 🧠 Копіюємо код проєкту
#COPY . .
#
## 🔄 Для коректного логування у Docker
#ENV PYTHONUNBUFFERED=1
#
## 🌍 Запускаємо Granian із правильними параметрами
#CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]

FROM python:3.12-slim

WORKDIR /app

# Системні залежності для psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо Python-залежності
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код
COPY . .

# Для коректного логування у Docker
ENV PYTHONUNBUFFERED=1

# Запуск Granian
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]
