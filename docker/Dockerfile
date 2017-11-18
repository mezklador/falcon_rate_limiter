FROM python:3.6

RUN pip install -U pip
RUN pip install -U falcon redis

EXPOSE 8088

COPY . /rate-limiter
WORKDIR /rate-limiter

CMD ["python", "/rate-limiter/app.py"]

