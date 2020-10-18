import csv
import glob
import os
from collections import defaultdict


class Client:
    def __init__(self, row,version,n):
        self.type = row[0]
        self.args = row[1]
        self.stdin = row[2]
        self.timestamp = float(row[3])
        self.version=version
        self.n = int(n)



def read_csv(path='.'):
    list_files = glob.glob(path+'/*.csv')
    clients = list()
    for csv_file in list_files:
        file=open(csv_file)
        csv_file= csv_file.replace('.\\','')
        csv_reader = csv.reader(file, delimiter=',')
        version,n=str(csv_file).replace('.csv','').split("_")
        for row in csv_reader:
            clients.append(Client(row,version,n))
        file.close()
    return clients




def group_by(clients):
    result = list()
    for c0 in clients:
        tmp=list()
        tmp.append(c0)
        clients.remove(c0)
        for c1 in clients:
            if c0.type==c1.type and c0.version==c1.version and c0.n == c1.n:
                tmp.append(c1)
                clients.remove(c1)
        result.append(tmp)
    return result