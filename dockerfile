FROM python:3.11.9

WORKDIR  /app

COPY requirements-ops.txt . . /app/

RUN pip install --upgrade pip 
RUN pip install -r requirements-ops.txt

CMD ["python", "-m", "uvicorn", "app.api:app", "--port", "8080", "--host", "0.0.0.0"]
EXPOSE 8080