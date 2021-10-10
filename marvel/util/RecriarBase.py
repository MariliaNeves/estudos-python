from marvel.entity import Endpoint
from marvel.service import StorieService, ComicService, SerieService, CreatorService, CharacterService
from marvel.util.GetDataMarvel import get_comics, get_values_endpoint, get_storie

endpoint = Endpoint.EndpointMarvel

def recriar_collection_Comic():
    comics = get_comics()
    ComicService.insert_all_comics(comics)
    return comics

def recriar_collection_Serie(uri_serie):
    series = get_storie(uri_serie)
    if series:
        SerieService.insert_all_series(series)

def recriar_collection_Creator(id_comic):
    creators = get_values_endpoint(endpoint.CREATORS.value, id_comic)
    if creators:
        CreatorService.insert_all_creators(creators)

def recriar_collection_Character(id_comic):
    characters = get_values_endpoint(endpoint.CHARACTERS.value, id_comic)
    if characters:
        CharacterService.insert_all_characters(characters)

def recriar_collection_Storie(id_comic):
    stories = get_values_endpoint(endpoint.STORIES.value, id_comic)
    if stories:
        StorieService.insert_all_stories(stories)

def delete_all():
    ComicService.delete_all_comics()
    SerieService.delete_all_series()
    CreatorService.delete_all_creators()
    CharacterService.delete_all_characters()
    StorieService.delete_all_stories()

def recriar():
    delete_all()
    lista = recriar_collection_Comic()
    for comic in lista:
        id_comic = comic['id']
        recriar_collection_Serie(comic['series']['resourceURI'])
        recriar_collection_Creator(id_comic)
        recriar_collection_Character(id_comic)
        recriar_collection_Storie(id_comic)