from bson.json_util import dumps
from flask import Flask, request
from pylint_af import PyLinter
import os
from marvel.service import SerieService, StorieService, connection
from marvel.service.CharacterService import CharacterService
from marvel.service.ComicService import ComicService
from marvel.service.CreatorService import CreatorService
from marvel.util.RecriarBase import recriar


app = Flask(__name__)
service_character = CharacterService(connection)
service_comic = ComicService(connection)
service_creator = CreatorService(connection)

@app.route('/restaurarBase', methods=['GET', ])
def recriarBase():
    recriar()
    return "Base restaurada."


### COMIC
@app.route('/comic/criar', methods=['POST', ])
def criar_comic():
    value = request.json
    service_comic.insert_comic(value)
    return "Criado com sucesso."


@app.route('/comic/alterar', methods=['PUT', ])
def alterar_comic():
    value = request.json
    id = request.args['id']
    service_comic.update_comic(id, value)
    return "Alterado com sucesso."


@app.route('/comic/buscar', methods=['GET', ])
def buscar_comic():
    lista = service_comic.get_all_comics()
    listaRetorno = []
    for comic in lista:
        print(f"comic {comic}")
        listaRetorno.append(comic)
    return str(listaRetorno)


@app.route('/comic/pesquisar', methods=['GET', ])
def pesquisar_comic():
    value = request.json
    comic = service_comic.get_comic(value)
    for item in comic:
        return dumps(item)
    return "Não encontrado!"


@app.route('/comic/deletar', methods=['DELETE', ])
def excluir_comic():
    id = request.args['id']
    service_comic.delete_comic(id)
    return "Excluído com sucesso."


### SERIE

@app.route('/serie/criar', methods=['POST', ])
def criar_serie():
    value = request.json
    SerieService.create_serie(value)
    return "Criado com sucesso."


@app.route('/serie/alterar', methods=['PUT', ])
def alterar_serie():
    value = request.json
    id = request.args['id']
    SerieService.update_serie(id, value)
    return "Alterado com sucesso."


@app.route('/serie/buscar', methods=['GET', ])
def buscar_serie():
    lista = SerieService.get_all_series()
    listaRetorno = []
    for serie in lista:
        print(f"serie {serie}")
        listaRetorno.append(serie)
    return str(listaRetorno)


@app.route('/serie/pesquisar', methods=['GET', ])
def pesquisar_serie():
    value = request.json
    serie = SerieService.get_serie(value)
    for item in serie:
        return dumps(item)
    return "Não encontrado!"


@app.route('/serie/deletar', methods=['DELETE', ])
def excluir_serie():
    value = request.json
    SerieService.delete_serie(value)
    return "Excluído com sucesso."


## CREATOR

@app.route('/creator/criar', methods=['POST', ])
def criar_creator():
    value = request.json
    service_creator.insert_creator(value)
    return "Criado com sucesso."


@app.route('/creator/alterar', methods=['PUT', ])
def alterar_creator():
    value = request.json
    service_creator.update_creator(value)
    return "Alterado com sucesso."


@app.route('/creator/buscar', methods=['GET', ])
def buscar_creator():
    lista = service_creator.get_all_creators()
    listaRetorno = []
    for creator in lista:
        print(f"creator {creator}")
        listaRetorno.append(creator)
    return str(listaRetorno)


@app.route('/creator/pesquisar', methods=['GET', ])
def pesquisar_creator():
    value = request.json
    creator = service_creator.get_creator(value)
    for item in creator:
        return dumps(item)
    return "Não encontrado!"


@app.route('/creator/deletar', methods=['DELETE', ])
def excluir_creator():
    id = request.args['id']
    service_creator.delete_creator(id)
    return "Excluído com sucesso."


### CHARACTER

@app.route('/character/criar', methods=['POST', ])
def criar_character():
    value = request.json
    service_character.insert_character(value)
    return "Criado com sucesso."


@app.route('/character/alterar', methods=['PUT', ])
def alterar_character():
    value = request.json
    id = request.args['id']
    service_character.update_character(id, value)
    return "Alterado com sucesso."


@app.route('/character/buscar', methods=['GET', ])
def buscar_character():
    lista = service_character.get_all_characters()
    listaRetorno = []
    for character in lista:
        print(f"character {character}")
        listaRetorno.append(character)
    return str(listaRetorno)


@app.route('/character/pesquisar', methods=['GET', ])
def pesquisar_character():
    value = request.json
    character = service_character.get_character(value)
    for item in character:
        return dumps(item)
    return "Não encontrado!"


@app.route('/character/deletar', methods=['DELETE', ])
def excluir_character():
    id = request.args['id']
    service_character.delete_character(id)
    return "Excluído com sucesso."


### STORIE

@app.route('/storie/criar', methods=['POST', ])
def criar_storie():
    value = request.json
    StorieService.create_storie(value)
    return "Criado com sucesso."


@app.route('/storie/alterar', methods=['PUT', ])
def alterar_storie():
    value = request.json
    id = request.args['id']
    StorieService.update_storie(id, value)
    return "Alterado com sucesso."


@app.route('/storie/buscar', methods=['GET', ])
def buscar_storie():
    lista = StorieService.get_all_stories()
    listaRetorno = []
    for storie in lista:
        print(f"storie {storie}")
        listaRetorno.append(storie)
    return str(listaRetorno)


@app.route('/storie/pesquisar', methods=['GET', ])
def pesquisar_storie():
    value = request.json
    storie = StorieService.get_serie(value)
    for item in storie:
        return dumps(item)
    return "Não encontrado!"


@app.route('/storie/deletar', methods=['DELETE', ])
def excluir_storie():
    value = request.json
    StorieService.delete_storie(value)
    return "Excluído com sucesso."


@app.route('/pylint', methods=['GET', ])
def run_pylint():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    PyLinter(dir_path).check()


app.run(debug=True)
