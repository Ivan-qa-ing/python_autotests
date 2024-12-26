import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f4e00524ce49442881b3dade4fbef833'
HEADER = {
    "trainer_token": "f4e00524ce49442881b3dade4fbef833",
    "Content-Type": "application/json"
}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_put = {
    "pokemon_id": "172221",
    "name": "generate",
    "photo_id": -1
}

body_add = {
    "pokemon_id": "172220"
}


# response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
# print(response.text)

# response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
# print (response_put.text)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print (response_add.text)