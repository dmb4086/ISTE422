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
import datetime

"""
    For readability I have divided the operations into 2 functions,
    file_handler just opens the JSON file and passes the objects to parser()
    which then models the data
"""

# assigning variables
list1 = []


def file_handler():
    with open("data.json") as json_file:
        data = json.load(json_file)

        parser(data)


def parser(data):
    count = 0
    for ele in data:
           if ele["creditcard"] is not None:
                count+=1
                list1.append(ele["name"]+ "," +ele["creditcard"])
    # print(list1[0])
    print("writing data of everyone without a credit card to file ")
    file_generator(list1)

def file_generator(data_list):

    # create a file with the name current date
    date = datetime.datetime.now()
    filename = str(date.year)+"" + str(date.month).zfill(2) + str(date.day).zfill(2)
    file = open(filename+".csv","w+")

    for entry in data_list:
        file.write(entry+"\n")

    print("File by the name of "+ filename+ ".csv populated")


if __name__ == '__main__':
   file_handler()