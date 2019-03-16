import requests
import json


chall_url = "https://cc.the-morpheus.de/challenges/8/"
solution_url = "https://cc.the-morpheus.de/solutions/8/"

resp = requests.get(chall_url).text
task = json.loads(resp)
k = task['k']
liste = task['list']

for a in range(len(liste)):
    for b in range(len(liste)):
        if liste[a] == liste[b]:
            print("found two equal elements")

                    
def searchIdexes(liste, k):
    for a in range(len(liste)):
        for b in range(a, len(liste)):
            for c in range(b, len(liste)):
                for d in range(c, len(liste)):
                    if liste[a] + liste[b] + liste[c] + liste[d] == int(k):
                        return [a, b, c, d]


def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


sendResult(searchIdexes(liste, k))


