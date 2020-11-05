import csv
import glob
import os
from collections import defaultdict
from model.setting import Setting
from model.outcome import Outcome
from model.group import Group
from model.plot import Plot


def read_settings(settings_filename):
    result = list()
    file = open(settings_filename, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        id, version, name, path, filename, extension, args, stdin, threads, iterations, concurrency, s_timestamp, d_graphs = row
        result.append(
            Setting(int(id), version, name, path, filename, extension, args, stdin, int(threads), int(iterations),
                    bool(concurrency),
                    float(s_timestamp), bool(d_graphs)))
    return result


def read_outcomes(outcomes_filename):
    result = list()
    file = open(outcomes_filename, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        id, timestamp = row
        result.append(Outcome(int(id), float(timestamp)))
    return result


def read_groups(groups_filename,outcomes_filename):
    result = list()
    file = open(groups_filename, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        id, outcomes_id, draw_templates, draw_avg = row[0:4]
        color = row[4:7]
        outcomes = read_outcomes(outcomes_filename)
        for outcome in outcomes:
            if outcome.id not in intoutcomes_id:
                outcomes.remove(outcome)
        result.append(Group(id, outcomes, color, draw_templates, draw_avg))
    return result


def read_plots(plots_file, groups_filename,outcomes_filename):
    result = list()
    file = open(plots_file, 'r')
    cvs_reader = csv.reader(file, delimiter=',')
    for row in cvs_reader:
        id = row[0]
        group_ids = row[1:]
        groups = read_groups(groups_filename,outcomes_filename)
        for group in groups:
            if group.id not in group_ids:
                groups.remove(group)
        result.append(Plot(int(id), groups))
    return result
