import os
from datetime import datetime

import matplotlib.pyplot as plt


def draw(groups):
    avgs=[]
    names=[]
    if not os.path.exists('../img'):
        os.mkdir('../img')
    for clients in groups:
        nums=[]
        count =0
        sum = 0
        for client in clients:
            nums.append(client.timestamp)
            sum+=client.timestamp
            count+=1
        avg=sum/count
        avgs.append(avg)
        names.append(client.type+'-'+client.version+'-'+str(client.n)+'-threads')
        plt.plot(nums)
        plt.ylabel('millisecondi')
        plt.xlabel('numero di chiamate')
        plt.axis([0, count, 0, 4*avg])
        plt.suptitle(client.type+' versione '+client.version+', con '+str(client.n)+' thread')
        path=('img/'+datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))

        if not os.path.exists(path):
            os.mkdir(path)

        plt.savefig(path+'/'+client.type+client.version+'-'+str(client.n)+'.png')
        plt.clf()
    path = 'img/'+'avg'
    if not os.path.exists(path):
        os.mkdir(path)
    size = len(avgs)
    plt.figure(figsize=(size,size/2))
    plt.bar(names, avgs)
    plt.suptitle('Media')
    plt.ylabel('millisecondi')
    plt.savefig(path+'/'+str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))+'.png')