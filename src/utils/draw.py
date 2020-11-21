import os
from datetime import datetime

import matplotlib.pyplot as plt


def draw(plots, settings):

    if not os.path.exists('../img'):
        os.mkdir('../img')

    for plot in plots:
        avgs = []
        names = []
        for group in plot.groups:
            sum = 0
            nums = []
            for outcome in group.outcomes:
                nums.append(outcome.timestamp)
                sum += outcome.timestamp
            avgs.append(sum / len(group.outcomes))
            for setting in settings:
                if setting.id == group.id:
                    break
            names.append(setting.name + '-' + setting.version + '-' + str(setting.threads) + '-threads' + '-' + str(
                setting.iterations) + '-iterations')
            plt.plot(nums, color=(0.5,0.1,0.6))
            plt.ylabel('secondi')
            plt.xlabel('numero di chiamata')
            plt.axis([0, len(group.outcomes), 0, 4 * avgs[0]])
        # plt.suptitle(plot.id)
        path = ('../img/' + datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
        if not os.path.exists(path):
            os.mkdir(path)
        plt.savefig(path + '/' + str(plot.id) + '.png')
        plt.clf()
        path = '../img/' + 'avg'
        if not os.path.exists(path):
            os.mkdir(path)
        size = len(avgs)
        plt.figure(figsize=(5*size, 5*size / 2))
        plt.bar(names, avgs)
        plt.suptitle('Media')
        plt.ylabel('Secondi')
        plt.savefig(path + '/' + str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")) + '.png')
