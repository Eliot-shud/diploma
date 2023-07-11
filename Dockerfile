FROM python:3.10-slim

# рабочая директория
WORKDIR /code

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка зависимостей
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip install -r requirements.txt

# копирование содержимого в контейнер
COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]