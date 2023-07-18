# Creating python endpoint 
import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {'title': 'Hello world my old friend', 
        'price': 129.99}

get_response = requests.put(endpoint, json=data) # http request psot

print(get_response.json()) # get respnse as JSON format

