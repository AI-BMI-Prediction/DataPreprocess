import pandas as pd
import openpyxl

#Sheet 1 엑셀 읽기
df1=pd.read_excel('data.xlsx',sheet_name='Sheet1')

#Sheet 2 엑셀 읽기
df2=pd.read_excel('data.xlsx',sheet_name='Sheet2')

#행 : cols, 열 : rows 이고 2차원 배열 생성
cols=3
rows=len(df1)
data=[[0 for j in range(cols)] for i in range(rows)]

#데이터 읽어오기
ID=df1['ID']
date=df1['collect_datetime']
value=df1['step_count']
for i in range(2929):
    data[i].append(ID[i])
    data[i].append(date[i])
    data[i].append(value[i])
    print(i," : ",ID[i],date[i],value[i])

# df_for_write=[]
# for i in range (len(ID)):
#     if(df1.index=ID[i])
