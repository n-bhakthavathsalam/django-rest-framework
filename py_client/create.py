# Creating python endpoint 
import requests

endpoint = "http://localhost:8000/api/products/"


data = {
    'title': 'this is field is done',
    'price': '23.09'

}
get_response = requests.post(endpoint, json=data) # http request psot
print(get_response.json()) # get respnse as JSON format

