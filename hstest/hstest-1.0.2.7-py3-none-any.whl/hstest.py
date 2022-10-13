### package base code 

# 필요 라이브러리 불러오기
import warnings
from ctgan import CTGANSynthesizer
from pycaret.classification import *
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 경고 메세지 무시
warnings.simplefilter(action='ignore', category=FutureWarning)

with warnings.catch_warnings():
    # ignore all caught warnings
    warnings.filterwarnings("ignore")
    # execute code that will generate warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

#  (1) 정형 데이터일 경우,
# 불균형 확인부 함수 선언

# 클래스 외부 함수 정의
# pycaret_acc : Pycaret 사용을 축약해 놓은 함수
def pycaret_acc(trd, label, test_data):
    warnings.filterwarnings('ignore')
    clf = setup(data = trd,test_data = test_data, target=label,data_split_shuffle=True, silent=True, normalize= True, fix_imbalance = False, session_id=42) 
    best_1 = compare_models(sort = 'Accuracy', n_select = 1, exclude=['dummy','svm','ridge'])

# origin : 데이터 입력 시, 처리 없이 그대로 반환함. 
def origin(x, label):
    # nothing
    return x

# imbalance_CTGAN : CTGAN 알고리즘을 이용하여,불균형 해소
def imbalance_CTGAN(x, label):
    #print(sum(train_data.Group==0), sum(train_data.Group==1) )
    #print(sum(test_data.Group==0), sum(test_data.Group==1) )
        
    # 라벨에 해당하는 "컬럼" 을 정의하는 문구가 필요함 
    # Group 을 라벨로 대체

    train_data_0= x[x[label]==x[label].unique()[0]]
    train_data_1= x[x[label]==x[label].unique()[1]]
    
    ### len(train_data_0 or 1)-len(train_data_1 or 0)개 생성
    maxa = max(len(train_data_0),len(train_data_1))
    mina = min(len(train_data_0),len(train_data_1))
    random_sample= maxa-mina
    
    if len(train_data_0) > len(train_data_1):

        data = train_data_1
        ctgan = CTGANSynthesizer(epochs=100)
        #ctgan.set_random_state(123)
        ctgan.fit(data,[label])
        samples_129_1 = ctgan.sample(random_sample)
        samples_129_1[label] = x[label].unique()[1]
        train_129 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
        train_data_ctgan =pd.concat([train_data_0 , train_129], axis = 0)
        return train_data_ctgan
    
    else : 
    
        data = train_data_0
        ctgan = CTGANSynthesizer(epochs=100)
        #ctgan.set_random_state(123)
        ctgan.fit(data,[label])
        samples_129_1 = ctgan.sample(random_sample)
        samples_129_1[label] = x[label].unique()[0]
        train_129 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
        train_data_ctgan =pd.concat([train_data_0 , train_129], axis = 0)
        return train_data_ctgan
    
def imbalance_CTGAN_2(x, label):
    #print(sum(train_data.Group==0), sum(train_data.Group==1) )
    #print(sum(test_data.Group==0), sum(test_data.Group==1) )
        
    # 라벨에 해당하는 "컬럼" 을 정의하는 문구가 필요함 
    # Group 을 라벨로 대체
    train_data_0= x[x[label]==x[label].unique()[0]]
    train_data_1= x[x[label]==x[label].unique()[1]]

    from ctgan import CTGANSynthesizer
    
    ctgan_1 = CTGANSynthesizer(epochs=100)
    ctgan_1.fit(train_data_1,[label])
    samples_129_1 = ctgan_1.sample(len(train_data_0))
    train_129_1 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
    train_129_1 = train_129_1.reset_index(drop=True)

    ctgan_0 = CTGANSynthesizer(epochs=100)
    ctgan_0.fit(train_data_0,[label])
    samples_129_0 = ctgan_0.sample(len(train_data_1))
    train_129_0 = pd.concat([train_data_0 ,samples_129_0 ], axis = 0 )
    train_129_0 = train_129_0.reset_index(drop=True)

    train_data_ctgan =pd.concat([train_129_0 , train_129_1], axis = 0)
    train_data_ctgan = train_data_ctgan.reset_index(drop=True)
    
    return train_data_ctgan

# imbalance_ADASYN : ADASYN 알고리즘을 이용하여,불균형 해소
def imbalance_ADASYN(x, label):
    ada = ADASYN(random_state=10)
    # 너무 적은 데이터 입력 시 -> 오류발생
    
    X, y = x.drop(label, axis = 1), x[label]
    X_res, y_res = ada.fit_sample(X, y)
    df_X_res = pd.DataFrame(X_res)
    df_y_res = pd.DataFrame(y_res)
    df_X_res.columns = X.columns
    #df_y_res.columns
    train_data_adasyn = pd.concat([df_X_res, df_y_res[label]] , axis = 1)
    return train_data_adasyn

# imbalance_UNDERSAMPLING : UNDERSAMPLING 알고리즘을 이용하여,불균형 해소  
def imbalance_UNDER(x, label):
    
    train_data_0= x[x[label]==x[label].unique()[0]]
    train_data_1= x[x[label]==x[label].unique()[1]]
    
    if len(train_data_0) > len(train_data_1) :
        train_data_under = pd.concat([train_data_0.sample(len(train_data_1)),train_data_1], axis = 0).reset_index(drop= True)
    else : 
        train_data_under = pd.concat([train_data_1.sample(len(train_data_0)),train_data_0], axis = 0).reset_index(drop= True)
    
    #print(train_data_under)
    return train_data_under
    #
    
# imbalance_SMOTE : SMOTE 알고리즘을 이용하여,불균형 해소
def imbalance_SMOTE(x, label):

    smote = SMOTE(random_state=0)
    X_train_over,y_train_over = smote.fit_sample(x.drop(label, axis = 1),x[label])
    train_data_smote = pd.concat([X_train_over, y_train_over], axis = 1) 
    return train_data_smote

# Pycaret 모델 출력값 중 정확도와 Model에 대해 반환함. 

def ttt(model,data,label, test_data):
    
    pycaret_acc(model(data, label), label, test_data)
    target_acc = pull()['Accuracy'][0]
    target_model = pull()['Model'][0]
    return target_acc,target_model      
    
class Main:
    data = {}
# 데이터 선언부
# 입력 함수 선언
# 
    def __init__(self, data):
        from sklearn.model_selection import train_test_split
        self.data = data
        self.label, self.list_im = Main.imbalance_judgment(self.data)

        X_train, X_test, Y_train, Y_test = train_test_split(data.drop(self.label ,axis = 1), data[self.label], test_size=0.3, random_state=42)
        self.train_data = pd.concat([X_train ,Y_train], axis =1)
        self.test_data = pd.concat([X_test ,Y_test], axis =1)

        Main.anomaly_replace(self, self.train_data, self.test_data)
        
        
        
#####################################################################################################
    
# label 결정 함수 선언
# label : 분류 목적 클래스에 대한 컬럼명 지정
    def input_label():
        #for test input
        #label = input("label_input : ")
        label = 'Group'
        if label == "exit" : 
            
            raise Exception('작동 종료')
        else:  
            pass
            return label

#####################################################################################################
    #
# 전처리 함수 선언
# 전처리부(이상치 대체, 결측값 대체)

    # 이상치 대체 함수 선언
    def anomaly_replace(self, train_data, test_data): 
        anomaly_data = self.data 
        self.train_data = train_data
        self.test_data = test_data
        # preprocessing -> anomaly_data 
        
        def winsorize_with_pandas(s, limits):
            return s.clip(lower=s.quantile(limits[0], interpolation='lower'),upper=s.quantile(1-limits[1], interpolation='higher'))

        # being preprocessing         
        # 결측값 대체 함수 선언
        def impute_data(train_data, test_data):
            columns = train_data.columns
            imputer_mice = IterativeImputer(random_state=83)
            imputed_train_data = imputer_mice.fit_transform(train_data)
            imputed_test_data = imputer_mice.transform(test_data)
            
            imputed_train_data = pd.DataFrame(imputed_train_data)
            imputed_train_data.columns = columns
            imputed_train_data = imputed_train_data.reset_index(drop=True)
            
            imputed_test_data = pd.DataFrame(imputed_test_data)
            imputed_test_data.columns = columns
            imputed_test_data = imputed_test_data.reset_index(drop=True)
            
            return imputed_train_data, imputed_test_data
            
        for i in anomaly_data.columns[:-1]:
            self.train_data[i] = pd.DataFrame(winsorize_with_pandas(self.train_data[i], limits=(0.1 ,0.1))) 
            self.test_data[i] = pd.DataFrame(winsorize_with_pandas(self.train_data[i], limits=(0.1 ,0.1)))
            
        imputed_data = impute_data(self.train_data, self.test_data)
        
        self.train_data, self.test_data = imputed_data

    #return 전처리된 데이터    


#####################################################################################################
# 불균형 확인부
# 데이터 클래스 불균형 여부(이상적인 데이터 클래스 균형 = 1:1 )에 의해 판단. 

    def imbalance_judgment(self):  
        label = Main.input_label()
        if len(self[label].unique()) <= 1 : 
                # 단일 Label 시 오류 출력
            print("label에 대한 입력이 잘못되었거나 단일 Label 데이터입니다.")
            imbalance_judgment(self)
                # break는 while 이나 for 문에서 사용
        else : 
            # label unique 확인
            list_label = []
            for i in range(len(self[label].unique())):
                list_label.append(self[label].unique()[i])
                # print((list_label)) 
                # label별 데이터 개수 확인
                tmp = []
                for i in list_label :
                    tmp.append(len(self[self[label]==i])) 
                value = int( max(tmp) == min(tmp))
            if max(tmp) == min(tmp) : 
                            # True : 1 
# 불균형 해소부
                print("불균형 없음")
                # 불균형이 없는 경우, 데이터 그대로 Pycaret 사용
                list_im = [origin]#[origin, imbalance_UNDER, imbalance_SMOTE, imbalance_ADASYN, imbalance_CTGAN]
                return  label, list_im        
            else :

                print("불균형 있음")
                            # False : 0 
                            # False ->  불균형이라고 판단함 
                # 불균형이 있는 경우, 데이터의 불균형을 해소 후 Pycaret 사용
                list_im = [origin, imbalance_UNDER, imbalance_SMOTE, imbalance_ADASYN, imbalance_CTGAN, imbalance_CTGAN_2]
                return  label, list_im   
#####################################################################################################

# 함수 선언
    def work_last(self):
        data = self.train_data
        test_data = self.test_data
        label = self.label 
        tmp = 0
        name = 0 
        i_iter = 0
        list_ls= []
        list_im = self.list_im
        for i in iter(list_im):
# 학습 단계 및 성능비교 단계 
            acc, model = ttt(i,data,label, test_data)
            idr = str(i.__name__)
            if tmp > acc:
                tmp = tmp
                name = model
            else : 
                tmp = acc
                name = model
                i_iter = str(i)
            list_ls.append([acc, model, idr])
# 출력부
        print(tmp, name, i_iter)  #1
        df_ls = pd.DataFrame(list_ls)
        print(df_ls)
        number = df_ls.index[  df_ls[0] == max(df_ls[0]) ]
        print(df_ls.iloc[number]) #2
        print("last_comparison_complete\n")
        
#####################################################################################################

#<실행 예> 

# 패키지 다운로드
#!pip install hstest
# 패키지 불러오기
#from inpack import hstest
# 클래스 정의
#a : 변수, x : 데이터 
#a = hstest.Main(x)

# 클래스 모듈 정의 및 결과 출력 
#a.work_last()
