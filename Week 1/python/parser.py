import json

def file_handler():
    with open("data.json") as json_file:
        data = json.load(json_file)

        parser(data)

list1 = []

def parser(data):
    count = 0
    for ele in data:
           if ele["creditcard"] is not None:
                count+=1
                list1.append(ele["name"])

    print(list1)





file_handler()