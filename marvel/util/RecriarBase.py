from marvel.entity import Endpoint
from marvel.service import StorieService, ComicService, SerieService, CreatorService, CharacterService
from marvel.util import GetDataMarvel

endpoint = Endpoint.EndpointMarvel

def recriar_collection_Comic():
    comics = GetDataMarvel.get_comics()
    print(f"comics {comics}")
    ComicService.insert_all_comics(comics)
    return comics

def recriar_collection_Serie(uri_serie):
    series = GetDataMarvel.get_serie(uri_serie)
    print(f"series {series}")
    if series:
        SerieService.insert_all_series(series)

def recriar_collection_Creator(id_comic):
    creators = GetDataMarvel.get_values_endpoint(endpoint.CREATORS.value, id_comic)
    print(f"creators {creators}")
    if creators:
        CreatorService.insert_all_creators(creators)

def recriar_collection_Character(id_comic):
    characters = GetDataMarvel.get_values_endpoint(endpoint.CHARACTERS.value, id_comic)
    print(f"characters {characters}")
    if characters:
        CharacterService.insert_all_characters(characters)

def recriar_collection_Storie(id_comic):
    stories = GetDataMarvel.get_values_endpoint(endpoint.STORIES.value, id_comic)
    print(f"stories {stories}")
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