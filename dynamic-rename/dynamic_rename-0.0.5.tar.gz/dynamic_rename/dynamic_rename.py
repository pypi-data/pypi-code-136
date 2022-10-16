import warnings
warnings.filterwarnings("ignore")
def dynamic_rename(df):
    df_col=[]
    for i in df.columns:
        df_col.append(i)
    for i in range(len(df_col)):
        print("current columns Name:" ,df_col[i])
        new_col_name=input('Kindly Enter renamed column name :')
        df=df.withColumnRenamed(df_col[i],new_col_name)
        print('column renamed to sucessfully to',new_col_name,'\n')
    return df