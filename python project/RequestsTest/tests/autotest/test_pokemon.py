import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/trainers'
TOKEN = 'f4e00524ce49442881b3dade4fbef833'
HEADER = {
    "trainer_token": "f4e00524ce49442881b3dade4fbef833",
    "Content-Type": "application/json"
}
TRAINER_ID = 12321

def test_status_code():
    response = requests.get(url = f'{URL}')  
    assert response.status_code == 200

def test_trainer_name():
        response = requests.get(url = f'{URL}', params = {'trainer_id' : TRAINER_ID})
        assert response.json()["data"][0]["trainer_name"] == 'dEsh'

    


    