import sys
sys.path.append("D:\Programs\Python\Python39\Lib\site-packages\mpqhsi")
from My_HSI import *

def HSI_Read_one_band(name1,name2,band=[80]):
    img = HSI_read_one_band(name1,name2,band)
    return img

def HSI_Read_3bands(name1,name2,bands=[14,35,64]):
    img = HSI_read_3bands(name1,name2,bands)
    return img

def HSI_Show1band(img,band = [70],title = 'title'):
    HSI_show_one_band(img,band,title)

def HSI_Show3bands(img,bands = [15,20,40],title = 'title'):
    HSI_show_3bands(img,bands,title)
    #显示伪彩色照片

def HSI_Show3D(img,bands=[15,50,70]):
    HSI_show_3D(img,bands)

def HSI_Savedir_graypic(in_path,out_oath,band=70):
    HSI_savedir_graypic(in_path,out_oath,band)
    #eg:../../data/HSI/test_data/,最后有'/'
    #将指定波段高光谱图像以灰度图形式保存到指定文件夹

def HSI_Savedir_rgbpic(in_path,out_oath,bands=[64,35,14]):
    HSI_savedir_rgbpic(in_path,out_oath,bands)
    #eg:../../data/HSI/test_data/,最后有'/'
    #将指定波段高光谱图像以灰度图形式保存到指定文件夹

def HSI_Meandata_make(in_path,out_path,band=80,gre_thre=100):
    result = HSI_meandata_make(in_path,out_path,band,gre_thre)
    return result

if __name__ == '__main__':
    from mpqhsi import *
    in_path = './test_data/'
    out_path = './'
    # result = HSI_meandata_make(in_path,out_path,band=80,thre=100)
    # result.to_csv('HSI_ROI_mean_data.csv',encoding='gb2312')

    # img = sp.envi.open('../../data/HSI/原始数据/正1-2.hdr', '../../data/HSI/原始数据/正1-2.cube')
    # # HSI_show_one_band(img,band=[70])
    # HSI_show_3D(img)
    # HSI_show_3bands(img,bands=[10,20,30])
    # HSI_savedirbgr_graypic('../../data/HSI/test_data/','./',band=80)
    # HSI_Savedir_rgbpic('./test_data/','./',bands=[15,35,64])
    # HSI_meandata_make('../../data/HSI/test_data/','./',gre_thre=100)
    # img = HSI_Read_one_band(r"D:\qiaozhiqi\Code\My_init\mpqhsi\mpqhsi-0.0.2\mpqhsi\test_data\反1-1.hdr",
    #                       r"D:\qiaozhiqi\Code\My_init\mpqhsi\mpqhsi-0.0.2\mpqhsi\test_data\反1-1.cube")

    img = HSI_Read_3bands(r"D:\qiaozhiqi\Code\My_init\mpqhsi\mpqhsi-0.0.2\mpqhsi\test_data\反1-1.hdr",
                          r"D:\qiaozhiqi\Code\My_init\mpqhsi\mpqhsi-0.0.2\mpqhsi\test_data\反1-1.cube")
    print(img.shape)
    cv2.imshow('a',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


