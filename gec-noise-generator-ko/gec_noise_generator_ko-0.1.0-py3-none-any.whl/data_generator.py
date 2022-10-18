from __future__ import absolute_import
import csv


def read_data(file_name):
    file = open(file_name, 'rt', encoding='UTF-8-sig')
    data = csv.reader(file)
    one_data = []
    two_data = []
    for line in data:
        one_data.append(line[0])
        two_data.append(line[1])
    file.close
    return one_data, two_data

def read_single_data(file_name):
    file = open(file_name, 'rt', encoding="UTF-8-sig")
    data = csv.reader(file)
    one_data = []
    for line in data:
        one_data.append(line[0])
    file.close
    return one_data
    
