import csv
import glob
import os
from collections import defaultdict
from model.config import Config
from model.service import Service
from model.group import Group


class Client:
    def __init__(self, row, version, n):
        self.type = row[0]
        self.args = row[1]
        self.stdin = row[2]
        self.timestamp = float(row[3])
        self.version = version
        self.n = int(n)


def read_configs(settings):
    result = list()
    file = open(settings, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        version, name, path, filename, extension, args, threads, stdin, s_timestapm, d_graphs = row
        result.append(Config(version, name, path, filename, extension, args, threads, stdin, s_timestapm, d_graphs))
    return result


def read_timestamps(timestamps):
    result = list()
    file = open(timestamps, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        version, name, args, threads, stdin, timestamp, s_timestapm, d_graphs,iterations = row
        result.append(Service(version, name, args, threads, stdin, timestamp, s_timestapm, d_graphs,iterations))
    return result


def read_groups(groups_file):
    result = list()
    file = open(groups_file, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        groupid, subgroupid, version, name, threads, stdin, draw_templates, draw_avg = row
        result.append(Group(groupid, subgroupid, version, name, threads, stdin, draw_templates, draw_avg))
    return result
