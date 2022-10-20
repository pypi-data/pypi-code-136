# This module is used to store environmental variables in ydnlp.

import os
import  requests

def _get_user_home():
    return os.path.expanduser('~')

def _get_ydnlp_home():
    if 'YDNLP_HOME' in os.environ:
        home_path = os.environ['YDNLP_HOME']
        if os.path.exists(home_path):
            if os.path.isdir(home_path):
                return home_path
            else:
                raise RuntimeError(
                    'The environment variable YDNLP_HOME {} is not a directory.'
                    .format(home_path))
        else:
            return home_path
    return os.path.join(_get_user_home(), '.ydnlp')

def _get_sub_home(directory, parent_home=_get_ydnlp_home()):
    home = os.path.join(parent_home, directory)
    if not os.path.exists(home):
        os.makedirs(home, exist_ok=True)
    return home


USER_HOME = _get_user_home()
YDNLP_HOME = _get_ydnlp_home()
MODEL_HOME = _get_sub_home('models')

NLP_MODEL ={
    'model':'https://winrobot-pub-a.oss-cn-hangzhou.aliyuncs.com/client/utility/ai_model/nlp/model/model.onnx',
    'dict':'https://winrobot-pub-a.oss-cn-hangzhou.aliyuncs.com/client/utility/ai_model/nlp/model/vocab.txt'
}

def download(url,path):
    '''
    从url路径中下载模型文件到path文件夹下
    '''

    fname = os.path.split(url)[-1]
    path = os.path.join(path,fname)
    session = requests.Session()
    session.trust_env = False
    response = session.get(url=url,  verify=False)
    
    if response.status_code != 200:
        raise RuntimeError("Downloading from {} failed with code "
        "{}!".format(url, response.status_code))
    with open(path,'wb') as file:
        file.write(response.content)
    

#  要判断是本地文件还是url
def download_model_name_or_path(pretrained_model_name_or_path):
    '''
     # pretrained_model_name_or_path (str): 模型的名字
     可以是：
     -  通用模型名
     -  定制场景模型名
     -  本地文件路径
    '''
    # print(MODEL_HOME)
    if os.listdir(MODEL_HOME) == []:
        # 下载模型
        download(NLP_MODEL[pretrained_model_name_or_path], MODEL_HOME)
        # 下载字典
        download(NLP_MODEL['dict'], MODEL_HOME)
    
# #下载模型
# download_model_name_or_path('models')

   

