import requests
import json
import ast

chall_url = "https://cc.the-morpheus.de/challenges/7/"
solution_url = "https://cc.the-morpheus.de/solutions/7/"

inputStr = requests.get(chall_url).text
inputDict = ast.literal_eval(inputStr)
inputList = inputDict['list']
inputK = inputDict['k']

print(inputK)
print(inputList)




def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


#sendResult()