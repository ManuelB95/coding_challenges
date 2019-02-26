import requests
import json

chall_url = "https://cc.the-morpheus.de/challenges/6/"
solution_url = "https://cc.the-morpheus.de/solutions/6/"

inputStr = requests.get(chall_url).text
decimalValue = int(inputStr)
binaryValue = ''

while decimalValue > 0:
    binaryValue = str(decimalValue % 2) + binaryValue
    decimalValue //= 2


def sendResult(result):
    data = {"token": result}
    result = requests.post(solution_url, json.dumps(data))
    print(result.text)


sendResult(binaryValue)
