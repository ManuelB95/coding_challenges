import requests
import json

chall_url = "https://cc.the-morpheus.de/challenges/5/"
solution_url = "https://cc.the-morpheus.de/solutions/5/"

inputStr = requests.get(chall_url).text


inputList = inputStr.split(' ')
length = len(inputList)

stack = []

for i in range(length):
    elem = inputList[i]
    if elem.isnumeric():
        stack.append(int(elem))
    else:
        b = stack.pop()
        a = stack.pop()
        if elem == '+':
            c = a + b
        elif elem == '-':
            c = a - b
        elif elem == '*':
            c = a * b
        elif elem == '/':
            c = a / b
        stack.append(c)

solution = int(stack.pop())


def sendResult(solution):
    data = {"token": solution}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)

sendResult(solution)
