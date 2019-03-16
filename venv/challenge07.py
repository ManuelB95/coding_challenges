import requests
import json
import ast

chall_url = "https://cc.the-morpheus.de/challenges/7/"
solution_url = "https://cc.the-morpheus.de/solutions/7/"

resp = requests.get(chall_url).text
task = json.loads(resp)
k = task['k']
liste = task['list']

solution = []

for elem in enumerate(liste):
    for i in range(elem[0] + 1, len(liste)):
        if elem[1] + liste[i] == k:
            solution = [elem[0], i]
            break
    if len(solution) > 0:
        break


def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


print(solution)
sendResult(solution)




