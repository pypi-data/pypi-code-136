# -*- encoding: utf-8 -*-
import csv
import numpy as np
import pandas as pd
import xlrd
import xlrd3
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

def copyright():
    """
    this file is edited by lry (c) 2020~2022
    """
    return None

def transfer_xlsx_to_csv(filename_old, filename_new):
    print(copyright.__doc__)
    file = csv.writer(open(filename_new, 'w', newline=''))
    try:
        data = xlrd.open_workbook(filename_old).sheet_by_index(0)
    except Exception as e:
        print(e)
        data = xlrd3.open_workbook(filename_old).sheet_by_index(0)
    finally:
        for r in range(data.nrows-1):
            file.writerow(data.row_values(r+1))
    print('transfer successfully!')

class Normalize():
    def MinMax(self,input_data):
        '''
            :param input_data:
            :return: output_data
            '''
        _range = np.max(input_data) - np.min(input_data)
        return (input_data - np.min(input_data)) / _range
    def ZScore(self,input_data):
        mu = np.mean(input_data, axis=0)
        sigma = np.std(input_data, axis=0)
        return (input_data - mu) / sigma

def read_csv_col(filename,col_id):
    data_0 = pd.read_csv(filename)
    print(data_0.shape)
    data_0 = data_0.values
    return data_0[:,col_id]

def draw_one_pic_box(num,title):
    '''
        :param num:
        :param title:
        :return:
        '''
    # 设置显示中文字体
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams['axes.unicode_minus'] = False
    plt.boxplot(num)
    plt.title(title)
    # plt.show()
    plt.savefig('example_' + title + '_刘仁宇.png')
    plt.close()

def get_num_info(num):
    length = len(num)
    i = 0
    sum = 0.0
    for i in range(length):
        sum = sum + float(num[i])
    avg = sum / length
    med = np.median(num)
    std = np.std(num)
    return avg, med, std

class detect():
    def statistics(self,avg,std,input_array,threshold=2):
        length = len(input_array)
        error_point = []
        #print(input_array,avg,std)
        for i in range(length):
            if input_array[i] < avg - threshold*std:
                error_point.append(i)
            if input_array[i] > avg + threshold*std:
                error_point.append(i)
        return error_point
    def Density_clustering(self,input_array):
        array_0 = input_array.reshape(-1,1)
        model = DBSCAN(eps=0.5, min_samples=5, metric='euclidean', algorithm='auto',leaf_size=30, p=None, n_jobs=1).fit_predict(array_0)
        print(model)
        error_point = []
        for i in range(len(input_array)):
            if model[i] == -1:
                error_point.append(i)
        return error_point

def show_pro3(input_array,error_index,photo_name):
    if len(error_index) == 0:
        print('无离群点')
        return
    ok_array = np.zeros(len(input_array)-len(error_index))
    error_array = np.zeros(len(error_index))
    ok = 0
    error = 0
    for i in range(len(input_array)):
        if i not in error_index:
            ok_array[ok] = input_array[i]
            ok = ok +1
        else:
            error_array[error] = input_array[i]
            error = error+1
    # draw pic
    plt.plot(ok_array,ok_array,'ob')
    plt.plot(error_array,error_array,'or')
    plt.title('lry'+photo_name)
    #plt.show()
    plt.savefig("lry"+photo_name+".png")
    plt.close()

def process(max_num,path):
    print(copyright.__doc__)
    str_0 = ['refractive_index','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']
    assert len(str_0) > max_num
    for i in range(max_num):
        a = read_csv_col(path,i)
        b = Normalize.MinMax(0,input_data=a)
        draw_one_pic_box(b,"归一化"+str_0[i]+"刘仁宇")
        avg,med,std = get_num_info(b)
        ans0 = detect.Density_clustering(0,b)
        ans1 = detect.statistics(0,avg,std,b)
        print(ans0,ans1)
        show_pro3(a,ans0,str_0[i]+"SCAN")
        show_pro3(a,ans1,str_0[i]+"3sigma")

if __name__ == '__main__':
    transfer_xlsx_to_csv('data.xlsx','data.csv')
    process(9,'data.csv')