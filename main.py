from bson.json_util import dumps
from flask import Flask, request

from marvel.service import ComicService
from marvel.util.GetDataMarvel import get_comics
from marvel.util.RecriarBase import recriar

app = Flask(__name__)

@app.route('/criar', methods=['POST',])
def criar():
    value = request.json
    ComicService.createComic(value)
    return "Criado com sucesso."

@app.route('/alterar', methods=['PUT',])
def alterar():
    value = request.json
    id = request.args['id']
    ComicService.updateComic(id, value)
    return "Alterado com sucesso."

@app.route('/buscar', methods=['GET',])
def buscar():
    lista = ComicService.getAllComics()
    listaRetorno = []
    for comic in lista:
        print(comic)
        listaRetorno.append(comic)
    return str(listaRetorno)

@app.route('/pesquisar', methods=['GET',])
def pesquisar():
    value = request.json
    comic = ComicService.getComic(value)
    for item in comic:
        return dumps(item)
    return "Não encontrado!"

@app.route('/deletar', methods=['DELETE',])
def excluir():
    value = request.json
    ComicService.deleteComic(value)
    return "Excluído com sucesso."

@app.route('/restaurarBase', methods=['GET',])
def recriarBase():
    recriar()
    return "Base restaurada."

app.run(debug=True)