FROM python:3.7

WORKDIR /usr/src/app

COPY setup.py README.md ./
COPY app/__init__.py ./app/__init__.py

RUN pip install -e .

EXPOSE 5000

COPY . .

ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini" ]