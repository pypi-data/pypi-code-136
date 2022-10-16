import os
import shutil
import time
from win32com.client import DispatchEx


from p2w4n.word import appendText, appendJPGFile, append

def pptx2word(file, max_slides=20, keep_images=False):
    file_name = os.path.splitext(file)[0]
    print(f'pptx2word:{file_name}')
    img_temp_folder = file_name + '_images'
    exported_word_folder = file_name + '_exported'
    word_file_prefix = file_name + '_4notion'

    # 打开 PowerPoint App


    # ppt = Dispatch('PowerPoint.Application')
    # 或者使用下面的方法，使用启动独立的进程：
    ppt = DispatchEx('PowerPoint.Application')

    # 如果不声明以下属性，运行的时候会显示的打开word
    ppt.Visible = 1  # 后台运行
    ppt.DisplayAlerts = 0  # 不显示，不警告

    try:
        pptSel = ppt.Presentations.Open(os.getcwd() + "\\" + file)
    except Exception as e:
        print(f'Open PPTX {file} failed: {e}')
        return

    if not os.path.exists(img_temp_folder):
        os.makedirs(img_temp_folder)
    
    if not os.path.exists(exported_word_folder):
        os.makedirs(exported_word_folder)
    
    
    # 打开 Word App
    word = DispatchEx('Word.Application')
    word.Visible = 0  # 后台运行 0，测试改为 1
    word.DisplayAlerts = 0  # 不显示，不警告

    # extract page to picture
    pptSel.SaveAs(os.getcwd() + "\\" + img_temp_folder, 17)
 

    # 主循环 
    tempDoc = word.Documents.Add()
    index = 0
    for slide in pptSel.Slides:
        index += 1
        print(f'slide：{index}')

        # add title of slide 
        appendText(tempDoc, f'\r\n>Slide: {index}')

        # copy slide
        # slide.Copy()
        # appendBMP(tempDoc)
        jpg = os.getcwd() + f"\\{img_temp_folder}\\Slide{index}.jpg"
        appendJPGFile(tempDoc, jpg)

        # copy notes
        tr = None
        if slide.NotesPage is not None:
            if slide.NotesPage.Shapes.Placeholders.Count > 1:
                tr = slide.NotesPage.Shapes.Placeholders(2).TextFrame.TextRange
        if not tr is None:
            txt = tr.Text
            if len(txt) > 0:
                tr.Copy()
                append(tempDoc)
        # time.sleep(0.1)

        if index % max_slides == 0:
            print(f'max_slide:{max_slides} reached index={index}, save file to ')
            tempDoc.SaveAs(os.getcwd() + f"\\{exported_word_folder}\\{word_file_prefix}-{index // max_slides}.docx"  )
            tempDoc.Close()
            tempDoc = word.Documents.Add()
    # save the last word file        
    tempDoc.SaveAs(os.getcwd() + f"\\{exported_word_folder}\\{word_file_prefix}-{index // max_slides + 1}.docx"  )
    tempDoc.Close()

    # clean up
    word.Quit()
    pptSel.Close()
    ppt.Quit()

    if not keep_images:
        shutil.rmtree(img_temp_folder)