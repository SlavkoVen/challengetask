# scheduler_trigger.Dockerfile

# Базовий образ з Pytho
FROM python:3.9-slim

# Встановлюємо залежності
RUN pip install --no-cache-dir Flask

# Копіюємо код програми
COPY scheduler_trigger.py /app/scheduler_trigger.py

# Визначаємо робочу директорію
WORKDIR /app

# Виставляємо порт для Flask
EXPOSE 8080

# Запускаємо програму
CMD ["python", "scheduler_trigger.py"]
