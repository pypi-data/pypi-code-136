import numpy as np
import pandas as pd 
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from hitrustai_lab.algorithm.ahp import AHPWeight

'''
auth_lable過濾auth code哪寫為異常
get_best_score : 算出整份auth預測與真實答案的最佳界線(多少policy_score以下為異常)
'''


def auth_lable(df_auth_columns, list_auth_code):
    return np.where((df_auth_columns.isin(list_auth_code)), 0, 1)


# get_best_score(df_new,"policy_score_fd","true_label")
def get_best_score(df_inpute_data, policy_score_col_name, true_label_col_name):
    arr_list = np.arange(-0.9, 1, 0.05)
    list_a = []
    list_b = []
    list_score = []
    for i in arr_list:
        df_inpute_data['predict_label'] = np.where((df_inpute_data[policy_score_col_name] < i), 0, 1)
        matrix = confusion_matrix(df_inpute_data[true_label_col_name], df_inpute_data['predict_label'])
        a = matrix[0][1]
        b = matrix[1][0]
        list_a.append(a)
        list_b.append(b)
        list_score.append(i)
    grades = {
        "ideal": list_a,
        "srcond_ideal": list_b,
        "score": list_score
    }
    df = pd.DataFrame(grades)
    exam_x = df['ideal']
    exam_y = df['srcond_ideal']

    x_train, x_test, y_train, y_test = train_test_split(
        exam_x, exam_y, train_size=.9)

    x_train = x_train.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    x_test = x_test.values.reshape(-1, 1)
    y_test = y_test.values.reshape(-1, 1)
    
    x1 = exam_x.values.reshape(-1, 1)
    y1 = exam_y.values.reshape(-1, 1)
    model = LinearRegression()

    model.fit(x1, y1)
    y_train_pred = model.predict(x1)
    s = np.absolute(y_train_pred - y1).astype(int)
    best_score = None
    min_ideal = None
    for i in np.where(s == min(s))[0]:
        m = df.loc[df.index == i]["score"].values[0]
        ideal = df.loc[df.index == i]["ideal"].values[0]

        if min_ideal is None:
            min_ideal = ideal
            best_score = round(m, 2)
        else:
            if min_ideal > ideal:
                min_ideal = ideal
                best_score = round(m, 2)
    return best_score
