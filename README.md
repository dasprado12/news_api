
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


## Como usar

    /news/petrobras
    /news/elon+musk
    /news/petrobras?when=2021-03-05
    /news/petrobras?before=2020-08-04
    /news/petrobras?after=2020-08-04
    /news/petrobras?after=2020-08-04&before=2020-09-29