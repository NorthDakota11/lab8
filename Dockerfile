FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask mysql-connector-python requests
EXPOSE 5000
CMD ["python", "app/main.py"]
