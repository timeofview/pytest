import csv
import os

class Client:
    def __init__(self, type, n, args, stdin, timestamp):
        self.type = type
        self.n = n
        self.args = args
        self.stdin = stdin
        self.timestamp = timestamp



def read_csv(path='.'):
    list_files = os.listdir(path+"*csv")
    for csv_file in list_files:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
