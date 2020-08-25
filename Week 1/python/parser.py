"""
@author Dev Bhatt

 - Assignment 1 using python

 - How to run this on your own machine:
        Go to the directory where parser.py is present on
        your computer by issuing the command 'cd' on your
        terminal ( cd $PATH )

        then simply type 'python parser.py'
"""
import json

# assigning variables
list1 = []

"""
    For readability I have divided the operations into 2 functions,
    file_handler just opens the JSON file and passes the objects to parser()
    which then models the data
"""
def file_handler():
    with open("data.json") as json_file:
        data = json.load(json_file)

        parser(data)


def parser(data):
    count = 0
    for ele in data:
           if ele["creditcard"] is not None:
                count+=1
                list1.append(ele["name"])

    print(list1)





file_handler()