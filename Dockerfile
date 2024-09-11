# Використовуйте офіційний образ Python
FROM python:3.9-slim

# Встановіть робочу директорію
WORKDIR /app

# Скопіюйте ваші файли в контейнер
COPY . .

# Встановіть залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запустіть ваш скрипт
CMD ["python", "https_trigger.py"]
