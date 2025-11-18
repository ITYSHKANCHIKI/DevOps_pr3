FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV SERVICE_B_URL=http://service_b:5001

EXPOSE 5000

CMD ["python", "app.py"]
