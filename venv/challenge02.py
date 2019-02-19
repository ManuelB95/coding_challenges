import requests
import json

chall_url = "https://cc.the-morpheus.de/challenges/2/"
solution_url = "https://cc.the-morpheus.de/solutions/2/"

"""
get the whole input as text
"""
inputStr = requests.get(chall_url).text


"""
get the k elem
"""
k = inputStr[inputStr.find(':')+2: inputStr.find(',')]


"""
get the list
"""
listStr = inputStr[inputStr.find('[')+1: inputStr.find(']')]
list = listStr.split(',')


"""
search k in list
"""
index = 0
for i, item in enumerate(list):
    if int(item) == int(k):
        index = i
        break


"""
post the solutijon
"""
data = {"token": index}
result = requests.post(solution_url, json.dumps(data))
print(result.text)
