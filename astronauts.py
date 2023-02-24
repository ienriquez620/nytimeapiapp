import requests
import main_functions

#API url
url = "http://api.open-notify.org/astros.json"

#Make the API request
#response = requests.get(url).json()

#Serialize the result to a JSON document
#main_functions.save_to_file(response,"astronauts.json")

#Deserialize the recently create JSON document
astronauts = main_functions.read_from_file("astronauts.json")

#What is the type of the object deserialized?
print(type(astronauts))

#What are its keys?
print(astronauts.keys())

#Access some of their values passing their keys
print(astronauts["message"])
print(astronauts["people"])
print(astronauts["number"])

#What are the names of the astronauts?
print(astronauts["people"][0]["name"])
print(astronauts["people"][1]["name"])
print(astronauts["people"][2]["name"])

#Print their names using a for loop
for i in astronauts["people"]:
    print(i["name"])


#Sort their names
