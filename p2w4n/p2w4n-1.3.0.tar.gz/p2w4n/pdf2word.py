import os
import shutil
import fitz
from win32com.client import DispatchEx

from p2w4n.word import appendText, appendJPGFile

def pdf2word(file, max_pages=20, keep_images=False):
    file_name = os.path.splitext(file)[0]
    print(f'pdf2word:{file_name}')
    img_temp_folder = file_name + '_images'
    exported_word_folder = file_name + '_exported'
    word_file_prefix = file_name + '_4notion'

    try:
        doc=fitz.open(file)
    except Exception as e:
        print(f'Open File {file} failed: {e}')
        return
    # doc = fitz.open(os.getcwd()+'\\'+file)
    if not os.path.exists(img_temp_folder):
        os.makedirs(img_temp_folder)
    
    if not os.path.exists(exported_word_folder):
        os.makedirs(exported_word_folder)
    
    
    # 打开 Word App
    word = DispatchEx('Word.Application')
    word.Visible = 0  # 后台运行 0，测试改为 1
    word.DisplayAlerts = 0  # 不显示，不警告

    # extract page to picture
    for index in range(0, doc.page_count):
        page = doc.load_page(index)
        jpg = page.get_pixmap()
        jpg.save(img_temp_folder + f'\\page-{index}.jpg')
    tempDoc = word.Documents.Add()

    # append it to a word doc
    for index in range(0, doc.page_count):
        print(f'page: {index}')

        # add title of slide 
        appendText(tempDoc, f'\r\n>Page: {index}')

        jpg = os.getcwd() + f"\\{img_temp_folder}\\page-{index}.jpg"
        appendJPGFile(tempDoc, jpg)
        if (index+1) % max_pages == 0:
            fname = os.getcwd() + f"\\{exported_word_folder}\\{word_file_prefix}-{(index+1) // max_pages}.docx"
            tempDoc.SaveAs(fname)
            print(f'max_pages[{max_pages}] reached index={index},, Save to a file: {fname}')
            tempDoc.Close()
            tempDoc = word.Documents.Add()

    # save the last word document
    # fname = os.getcwd() + f"\\{word_file_prefix}-{((index+1) // max_pages)+1}.docx" 
    fname = os.getcwd() + f"\\{exported_word_folder}\\{word_file_prefix}-{(index+1) // max_pages}.docx"
    print(f'index={index}, Final file save to {fname}')
    tempDoc.SaveAs( fname) 
    tempDoc.Close()
    word.Quit()
    if not keep_images:
        shutil.rmtree(img_temp_folder)