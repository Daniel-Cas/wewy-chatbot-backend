FROM python:3.10

WORKDIR /code

COPY ./requeriments.txt /code/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt

COPY ./api /code/api

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8080"]
