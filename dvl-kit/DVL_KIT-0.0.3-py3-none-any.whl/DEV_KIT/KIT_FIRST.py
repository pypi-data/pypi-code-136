
def View_a_list_of_files_in_a_folder() :
    '''[출처] 사무 SW용 파이썬 자주 사용하는 코드 공유|작성자 잔마왕
    from tkinter import filedialog
    import os

    foldername = filedialog.askdirectory()

    filearr = os.listdir(foldername)

    for file in filearr:
        print(file)
    '''
    from tkinter import filedialog
    import os

    foldername = filedialog.askdirectory()

    filearr = os.listdir(foldername)

    for file in filearr:
        print(file)

def View_a_list_of_files_in_a_folder_extension_filter_added() :
    '''사무 SW용 파이썬 자주 사용하는 코드 공유|작성자 잔마왕
    from tkinter import filedialog
    import os
    import re

    foldername = filedialog.askdirectory()

    files = [f for f in os.listdir(foldername) if re.match('.*[.]확장자명', f)]

    for file in files:
        print(file)
    '''
    from tkinter import filedialog
    import os
    import re

    foldername = filedialog.askdirectory()

    files = [f for f in os.listdir(foldername) if re.match('.*[.]확장자명', f)]

    for file in files:
        print(file)

def area_of_triangle(height, length_of_the_base) :
    area = height * length_of_the_base / 2
    return area

def area_of_square(height, length_of_the_base) :
    area = height * length_of_the_base
    return area