import requests
import json

challUrl_11 = "https://cc.the-morpheus.de/challenges/11/"


chall_url = "https://cc.the-morpheus.de/challenges/1/"
solution_url = "https://cc.the-morpheus.de/solutions/1/"

resp = requests.get(chall_url)
data = {"token": resp.text}


result = requests.post(solution_url, json.dumps(data))
print(result.text)
