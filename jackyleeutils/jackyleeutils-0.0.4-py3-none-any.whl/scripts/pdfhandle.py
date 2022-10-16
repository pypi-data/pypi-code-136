import PyPDF2

def print_pdf_info(file_name:str, open_mode:str="rb"):
  """
  读取pdf内容
  参数：
    file_name str : 文件名，比如 "test.pdf"
    open_mode str : 打开方式，比如 "rb"
  返回值：
  """
  with open(file_name, open_mode) as file:
    reader = PyPDF2.PdfFileReader(file) # 创建reader对象
    page = reader.getPage(0) # 第一页的索引是0
    page.rotateCounterClockwise(90) # 方法：顺时针旋转90°，注意，这不会修改原文件，只是修改内存中的对象
    print(f"this pdf has {reader.numPages} pages.") 
    print(page.scale, page.scaleBy, page.scaleTo)


def rotate(file_name:str, open_mode:str="rb", angle:int=90):
  """
  旋转pdf内容
  参数：
    file_name str : 文件名，比如 "test.pdf"
    open_mode str : 打开方式，比如 "rb"
    angle     int : 逆时针旋转角度，比如旋转90°，值为 90
  返回值：
  """
  writer = PyPDF2.PdfFileWriter() # 创建writer对象
  with open(file_name, open_mode) as file:
    reader = PyPDF2.PdfFileReader(file)
    for i in range(reader.numPages):
      page = reader.getPage(i)
      page.rotateCounterClockwise(angle)
      writer.addPage(page)
      # writer.insertPage(page,index=1) # 可以在第1页插入新页面
      # writer.insertBlankPage() # 可以插入空白页面
    with open("rotate.pdf", "wb") as output:
        writer.write(output)


def merge(file_names:list[str], output_name:str) -> None:
  """
  合并pdf文件
  参数：
    files_names: 文件名列表，比如 ["test1.pdf", "test2.pdf"]
    output_name: 导出的文件名，比如 "merged.pdf"
  返回值：
    None
  """
  merger = PyPDF2.PdfFileMerger() # 创建合并对象
  for file_name in file_names:
    merger.append(file_name)
  merger.write(output_name)
