import pandas as pd
import openpyxl

def ComputeDate(string):
    if(string=="2022-07-14"): return 0
    elif(string=="2022-07-15"): return 1
    elif(string=="2022-07-16"): return 2
    elif(string=="2022-07-17"): return 3
    elif(string=="2022-07-18"): return 4
    elif(string=="2022-07-19"): return 5
    elif(string=="2022-07-20"): return 6
    elif(string=="2022-07-21"): return 7
    elif(string=="2022-07-22"): return 8
    elif(string=="2022-07-23"): return 9
    elif(string=="2022-07-24"): return 10
    elif(string=="2022-07-25"): return 11
    elif(string=="2022-07-26"): return 12
    elif(string=="2022-07-27"): return 13
    elif(string=="2022-07-28"): return 14
    elif(string=="2022-07-29"): return 15
    elif(string=="2022-07-30"): return 16
    elif(string=="2022-07-31"): return 17
    elif(string=="2022-08-01"): return 18
    elif(string=="2022-08-02"): return 19
    elif(string=="2022-08-03"): return 20
    elif(string=="2022-08-04"): return 21
    elif(string=="2022-08-05"): return 22
    elif(string=="2022-08-06"): return 23
    elif(string=="2022-08-07"): return 24
    elif(string=="2022-08-08"): return 25
    elif(string=="2022-08-09"): return 26
    elif(string=="2022-08-10"): return 27
    elif(string=="2022-08-11"): return 28
    elif(string=="2022-08-12"): return 29
    elif(string=="2022-08-13"): return 30
    elif(string=="2022-08-14"): return 31
    elif(string=="2022-08-15"): return 32
    elif(string=="2022-08-16"): return 33
    elif(string=="2022-08-17"): return 34
    elif(string=="2022-08-18"): return 35
    elif(string=="2022-08-19"): return 36
    elif(string=="2022-08-20"): return 37
    elif(string=="2022-08-21"): return 38
    elif(string=="2022-08-22"): return 39
    elif(string=="2022-08-23"): return 40
    elif(string=="2022-08-24"): return 41
    elif(string=="2022-08-25"): return 42
    elif(string=="2022-08-26"): return 43

#Sheet 1 엑셀 읽기
df1=pd.read_excel('data.xlsx',sheet_name='Sheet1')

#Sheet 2 엑셀 읽기
df2=pd.read_excel('data.xlsx',sheet_name='Sheet2')

#행 : cols, 열 : rows 이고 2차원 배열 생성
cols=3
rows=len(df1)
data=[[0 for j in range(cols)] for i in range(rows)]

#시트 1에서 데이터 읽어오기
Sheet1_ID=df1['ID']
Sheet1_date=df1['collect_datetime']
Sheet1_value=df1['step_count']
for i in range(len(df1)):
    data[i][0]=Sheet1_ID[i]
    data[i][1]=Sheet1_date[i]
    data[i][2]=Sheet1_value[i]

Sheet2_ID=df2['ID'] #ID
cols=len(Sheet2_ID)
rows=len(df2)
df_for_write_array=[[0 for j in range(cols)] for i in range(rows)]
# 배열에 값을 추가하는 부분
for i in range(len(df1)):
    for j in range(len(df2)):
        if(Sheet2_ID[j]==data[i][0]):
            index=ComputeDate(data[i][1])
            df_for_write_array[j][index]=data[i][2]

#엑셀에 쓰는 부분
df_for_write=pd.DataFrame(df_for_write_array)
df_for_write.to_excel("inp.xlsx",sheet_name="Sheet2")