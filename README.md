
# Scrapping_API

API responsável por fazer o scrapping de notícias e expor estes dados no formato json

## Requisitos

[Python](https://www.python.org/)
[Docker](https://docs.docker.com/engine/install/ubuntu/)

  

## Como rodar

É possível rodar a aplicação de duas formas:

### Uwsgi

    python3 -m venv venv
    source venv/bin/activate
    pip install -e .
    uwsgi --ini uwsgi.ini

### Docker
    docker build -t scrapping .
    docker run -p 5000:5000 scrapping

