import requests
import json
import ast

chall_url = "https://cc.the-morpheus.de/challenges/4/"
solution_url = "https://cc.the-morpheus.de/solutions/4/"


inputStr = requests.get(chall_url).text
inputDict = ast.literal_eval(inputStr)
inputList = inputDict['list']
inputK = inputDict['k']


length = len(inputList)
n = inputK // length
inputKShorten = inputK - n * length
sliceIndex = length - inputKShorten


rotatedList = inputList[sliceIndex:] + inputList[:sliceIndex]


def sendResult(inputList):
    data = {"token": inputList}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


sendResult(rotatedList)
