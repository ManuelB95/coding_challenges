import requests
import json

chall_url = "https://cc.the-morpheus.de/challenges/7/"
solution_url = "https://cc.the-morpheus.de/solutions/7/"

resp = requests.get(chall_url).text
task = json.loads(resp)
k = task['k']
liste = task['list']

def searchIndexes(liste, k):
    hashMap = dict()
    for i in range(len(liste)):
        complement = k - liste[i]
        if complement in hashMap:
            return [hashMap[complement], i]
        hashMap[liste[i]] = i
    

def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


sendResult(searchIndexes(liste, k))
