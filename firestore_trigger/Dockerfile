# Базовий образ Python
FROM python:3.9-slim

# Встановлюємо необхідні пакети
RUN pip install --no-cache-dir Flask
#RUN pip install --no-cache-dir functions-framework

# Копіюємо файл із функцією
COPY firestore_trigger.py /app/firestore_trigger.py

# Визначаємо робочу директорію
WORKDIR /app

# Виставляємо порт 8080 для Cloud Run
EXPOSE 8080

# Запускаємо сервер functions-framework, вказуючи, яка функція буде використовуватися
CMD ["python", "firestore_trigger.py"]
#CMD ["functions-framework", "--target=firestore_trigger", "--port=8080"]
