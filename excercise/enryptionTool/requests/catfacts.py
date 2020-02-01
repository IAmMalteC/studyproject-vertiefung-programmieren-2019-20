import json
import requests


# api documentation: https://alexwohlbruck.github.io/cat-facts/docs/


def print_random_fact(animal_type: str):
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
    response_body = response.json()  # parse response into json dictionary
    print("A random fact for cat is: \n", response_body["text"])  # access json dictionary field "text"
