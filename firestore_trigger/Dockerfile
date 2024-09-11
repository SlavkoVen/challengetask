# firestore_trigger.Dockerfile

# Базовий образ з Python
FROM python:3.9-slim

# Встановлюємо залежності
RUN pip install --no-cache-dir google-cloud-firestore Flask

# Копіюємо код програми
COPY firestore_trigger.py /app/firestore_trigger.py

# Визначаємо робочу директорію
WORKDIR /app

# Виставляємо порт для Flask (якщо це потрібно для Firestore)
EXPOSE 8080

# Запускаємо програму
CMD ["python", "firestore_trigger.py"]
