# Creating python endpoint 
import requests

# endpoint = "http://httpbin.org/"
endpoint = "http://localhost:8000/api"

# get_response = requests.get(endpoint, json={"product_id":123}) # http request for get
get_response = requests.post(endpoint, json={"title":"Hello World!"}) # http request psot

# print(get_response.text) # print raw text response
# print(get_response.status_code)

print(get_response.json()) # get respnse as JSON format

