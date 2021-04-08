from flask import Flask, jsonify, request
from app.app import search_news

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def default():
        return jsonify({'message': "A aplicação está rodando"})

    @app.route("/news/<termo>", methods=["GET"])
    def news(termo):
        args = request.args
        return jsonify(search_news(termo, args))

    return app