"""
@Project:bailan_bad
@File:bad_recognition.py
@Author:郑智
@Date:14:11
""" 
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
def bubble_sort():
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
print(bubble_sort())