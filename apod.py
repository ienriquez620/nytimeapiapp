import main_functions
import requests

# NASA's API url
url = "https://api.nasa.gov/planetary/apod?api_key="

# Read your NASA API key

api_keys = main_functions.read_from_file("api_keys.json")
api_key = api_keys["nasa_api"]
#print(api_key)

#Build the final API url
final_url = url + api_key

#Make the API request
#response = requests.get(final_url).json()

#Serialize the result to a JSON document
#main_functions.save_to_file(response,"apod.json")

#Deserialize the recently create JSON document
apod =main_functions.read_from_file("apod.json")

#What is the type of the object deserialized?
print(type(apod))

#What are its keys?
print(apod.keys())

#Access some of their values passing their keys
print(apod["date"])
print(apod["title"])
print(apod["explanation"])
print(apod["url"])