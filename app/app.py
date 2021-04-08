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
    else:
        return "when:1d"
    # return "when:{}".format(args.get('when')) if args.get('when') else return "when:1d"
    # if(args.get('after')):
    #     return "afer:{}".format(args.get('after'))
    # if(args.get('before')):
    #     return "before:{}".format(args.get('before'))

def search_news(termo="petrobras", search_args={}):
    # nltk.download('stopwords')
    periodo=dict2text(search_args)
    # https://news.google.com/rss/search?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&oc=11&q=petrobras+when:1d
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