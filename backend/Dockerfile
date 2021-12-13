FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=2000", "--reload" ]
