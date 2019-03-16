import requests
import json


chall_url = "https://cc.the-morpheus.de/challenges/8/"
solution_url = "https://cc.the-morpheus.de/solutions/8/"

resp = requests.get(chall_url).text
task = json.loads(resp)
k = task['k']
liste = task['list']


                    
def searchIdexes(liste, k):
    leange = len(liste)
    for a in range(leange):
        for b in range(a, leange):
            for c in range(b, leange):
                for d in range(c, leange):
                    if liste[a] + liste[b] + liste[c] + liste[d] == int(k):
                        print("hi")
                        return [a, b, c, d]


#print(searchIdexes(liste, k))


def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


sendResult(searchIdexes(liste, k))


