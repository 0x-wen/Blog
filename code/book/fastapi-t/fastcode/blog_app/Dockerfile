FROM python:3.10-slim

COPY . /var/www/src
WORKDIR /var/www/src

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]