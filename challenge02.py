import requests
import json


chall_url = "https://cc.the-morpheus.de/challenges/2/"
solution_url = "https://cc.the-morpheus.de/solutions/2/"

resp = requests.get(chall_url)

#ab hier aufgabe:

print(resp.text)



#data = {"token": resp.text}
#result = requests.post(solution_url, json.dumps(data))
#print(result.text)
