import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
  params = {"X-Api-Key": API_KEY}

  response = requests.get(url, params=params)
  if response.status_code == 200 and response.json() != []:
      data = response.json()
      return data
  else:
      print("Response code:", response.status_code)
      print(f"Animal {animal} NOT found")
      no_such_animal = [animal]
      return no_such_animal