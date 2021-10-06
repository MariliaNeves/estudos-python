from marvel.entity import Endpoint
from marvel.service import StorieService, ComicService, SerieService, CreatorService, CharacterService
from marvel.util.GetDataMarvel import get_comics, get_values_endpoint

endpoint = Endpoint.EndpointMarvel

def recriar_collection_Comic():
    ComicService.delete_all_comics()
    comics = get_comics()
    ComicService.insert_all_comics(comics)

def recriar_collection_Serie(id_comic):
    SerieService.delete_all_series()
    series = get_values_endpoint(endpoint.SERIES.value, id_comic)
    if series:
        SerieService.insert_all_series(series)

def recriar_collection_Creator(id_comic):
    CreatorService.delete_all_creators()
    creators = get_values_endpoint(endpoint.CREATORS.value, id_comic)
    print(f"creators {creators}")
    if creators:
        CreatorService.insert_all_creators(creators)

def recriar_collection_Character(id_comic):
    CharacterService.delete_all_characters()
    characters = get_values_endpoint(endpoint.CHARACTERS.value, id_comic)
    if characters:
        CharacterService.insert_all_characters(characters)

def recriar_collection_Storie(id_comic):
    StorieService.delete_all_stories()
    stories = get_values_endpoint(endpoint.SERIES.value, id_comic)
    if stories:
        StorieService.insert_all_stories(stories)

def recriar():
    recriar_collection_Comic()
    lista = ComicService.get_all_comics()
    for comic in lista:
        id_comic = comic['id']
        #recriar_collection_Serie(id_comic)
        recriar_collection_Creator(id_comic)
        #recriar_collection_Character(id_comic)
        #recriar_collection_Storie(id_comic)