import requests
import json

BASE = "http://127.0.0.1:5000"  # The link that is generated when you run the main file

# response = requests.get(BASE + "/helloworld/Beray/21")  # This is how you get the requests
# # (first with the word, then the info)
# response2 = requests.get(BASE + "/test/Beray")
# print(response.json())  # print
# print(response2.json())

headers = {'Content-Type': 'application/json'}
# data = json.dumps({"likes": 10, "name": "Beray", "views": 100000, "comments": 10000})
# response3 = requests.put(BASE + "/video/1", data=data, headers=headers)
# print(response3.json())
# input()
# response3 = requests.get(BASE + "/video/1")
# print(response3.json())

data2 = [{"likes": 10, "name": "Beray", "views": 100000, "comments": 10000},
                   {"likes": 20, "name": "Edis", "views": 2333, "comments": 2},
                   {"likes": 30, "name": "Aynur", "views": 100111000, "comments": 1}]
for i in range(len(data2)):
    response4 = requests.put(BASE + "/video/" + str(i), json=data2[i], headers=headers)
    print(response4.json())

input()
response4 = requests.delete(BASE + "/video/0")
print(response4)
input()
response4 = requests.get(BASE + "/video/2")
print(response4.json())

# IMPORTANT, when you have a list of dictionaries, you dont need json.dumps(), only on strings!
