from bson.json_util import dumps
from flask import Flask, request
import requests, DB


app = Flask(__name__)

api_url = 'http://gateway.marvel.com/v1/public/comics?ts=1&apikey=d29f2a6da246c726d68defcee236fc60&hash=89f999eda91e5deddee3d1aadb583e91'
response = requests.get(api_url)

@app.route('/criar', methods=['POST',])
def criar():
    value = request.json
    DB.createComic(value)
    return "Criado com sucesso."

@app.route('/alterar', methods=['PUT',])
def alterar():
    value = request.json
    id = request.args['id']
    print(id, value)
    DB.updateComic(id, value)
    return "Alterado com sucesso."

@app.route('/buscar', methods=['GET',])
def buscar():
    lista = DB.getAllComics()
    listaRetorno = []
    for comic in lista:
        print(comic)
        listaRetorno.append(comic)
    return str(listaRetorno)


@app.route('/pesquisar', methods=['GET',])
def pesquisar():
    value = request.json
    comic = DB.getComic(value)
    for item in comic:
        return dumps(item)
    return "Não encontrado!"


@app.route('/deletar', methods=['DELETE',])
def excluir():
    value = request.json
    DB.deleteComic(value)
    return "Excluído com sucesso."

@app.route('/restaurarBase', methods=['GET',])
def recriarBase():
    DB.deleteAllComics()
    comics = getDataComics()
    DB.insertAllComics(comics)
    return "Base restaurada."


def getDataComics():
    jsonResult = response.json()
    data = jsonResult['data']
    comics = data['results']
    return comics

app.run(debug=True)