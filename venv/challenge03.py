import requests
import json
import ast

chall_url = "https://cc.the-morpheus.de/challenges/3/"
solution_url = "https://cc.the-morpheus.de/solutions/3/"

"""
get the input datas
"""
inputStr = requests.get(chall_url).text
inputDict = ast.literal_eval(inputStr)
inputList = inputDict['list']
inputK = inputDict['k']


"""
sort the list from high to low
"""
n = len(inputList)
for i in range(n-1):
    for j in range(n-i-1):
      if inputList[j] < inputList[j+1]:
        tmp = inputList[j]
        inputList[j] = inputList[j+1]
        inputList[j+1] = tmp



"""
inputK - 1 is the index in list of the kth maximum
"""
result = inputList[inputK-1]



"""
post the solutijon
"""
data = {"token": result}
result = requests.post(solution_url, json.dumps(data))
print(result.text)