# Creating python endpoint 
import requests

endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint) # http request psot

print(get_response.json()) # get respnse as JSON format

