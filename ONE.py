import requests
import random
from pprint import pprint
character_number = random.randint
url = 'http://hp-api.herokuapp.com/api/characters'.format(character_number)
response = requests.get(url)
print(response)
harry_potter = response.json()