# https_trigger.Dockerfile

# Базовий образ з Python
FROM python:3.9-slim

# Встановлюємо залежності
RUN pip install --no-cache-dir Flask

# Копіюємо код програми
COPY https_trigger.py /app/https_trigger.py

# Визначаємо робочу директорію
WORKDIR /app

# Виставляємо порт для Flask
EXPOSE 8080

# Запускаємо програму
CMD ["python", "https_trigger.py"]
