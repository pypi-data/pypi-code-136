import pandas as pd
import pickle
from sklearn import metrics
from ctypes import cdll, c_char_p
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


return_code = {
    'pred_success': '4003',                 # 預測成功
    'pred_fail': '9905',                    # 預測失敗
    'container_start_success': '4006',      # 容器啟動成功
    'container_start_fail': '4008',         # 容器啟動失敗
    'train_success': '4007',                # 小模型訓練成功
    'train_all_success': '4008',            # 大模型訓練成功
    'train_fail': '9909',                   # 訓練失敗
    'train_save_fail': '9916',              # 知識庫儲存失敗
    'train_load_fail': '9913',              # 知識庫載入失敗
    'train_valid_fail': '9914',             # 驗證失敗
}


def decrypt_passwd(so_name, passwd):
    try:
        lib = cdll.LoadLibrary(so_name)
        lib.passedDecrypt.argtypes = [c_char_p]
        lib.passedDecrypt.restype = c_char_p
        password = lib.passedDecrypt(passwd.encode()).decode()
        return password
    except Exception:
        return passwd


def open_connection(db_uri):
    engine = create_engine(db_uri, echo=False)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return (session)


def close_connection(session):
    session.close()


class AITrainUtilsAPI:
    def save_variable(self, v, filename):
        f = open(filename, 'wb')
        pickle.dump(v, f)
        f.close()
        return filename

    def load_variavle(self, filename):
        f = open(filename, 'rb')
        r = pickle.load(f)
        f.close()
        return r

    def err_reason(self, e):
        error_class = e.__class__.__name__
        detail = e.args[0]
        errMsg = "[{}] {}".format(error_class, detail)
        return errMsg

    def report(self, return_code, accuracy=-1, precision=-1, recall=-1, f1=-1, reason="nan"):
        return {
            'return_code': return_code,
            "report": {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1
            },
            "reason": reason
        }

    def confuse_classification_report(self, test_y, test_y_predicted):
        accuracy = round(metrics.accuracy_score(test_y, test_y_predicted), 2)
        precision = round(metrics.precision_score(test_y, test_y_predicted), 2)
        recall = round(metrics.recall_score(test_y, test_y_predicted), 2)
        f1 = round(metrics.f1_score(test_y, test_y_predicted), 2)
        return self.report("4007", accuracy, precision, recall, f1)
