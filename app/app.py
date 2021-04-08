from flask import Flask, jsonify
from nltk.corpus import stopwords
import feedparser
import nltk
import datetime
# from newsplease import NewsPlease


'''
    when: 1h (Ultima hora), 1d (Ultimas 24h), 7d (Ultima semana), 1y (Ultimo ano)
    when: datetime iso format <2020-04-04T20:10:34>
    after: datetime iso format
    before: datetime iso format
'''

def dict2text(args):
    if(args.get("when")):
        return "when:".format(args.get("when"))
    if(args.get("after") and args.get("before")):
        return "after:{}&before:{}".format(args.get("after"), args.get("before"))
    if(args.get("after")):
        return "after:{}".format(args.get("after"))
    if(args.get("before")):
        return "before:{}".format(args.get("before"))
    else:
        return "when:1d"

def search_news(termo="petrobras", search_args={}):
    # nltk.download('stopwords')
    periodo=dict2text(search_args)
    url_pesquisa = "https://news.google.com/rss/search?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&oc=11&q={0}+{1}".format(termo,periodo)
    feed = feedparser.parse(url_pesquisa).entries

    _arr = []

    for i in range(len(feed)):
        _arr.append({
            "title": feed[i]['title'],
            "date": datetime.datetime.strptime(feed[i]['published'], '%a, %d %b %Y %H:%M:%S %Z').isoformat(),
            "link": feed[i]['link'],
            "company": feed[i]['source']['title'],
            "link_company": feed[i]['source']['href'],
        })

    return _arr