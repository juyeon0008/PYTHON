
"""
거북이 프로젝트 - 학점 계산기 (데이터프레임)
"""
import pandas as pd
import numpy as np

df = pd.DataFrame()

All_Grade = pd.DataFrame(columns= ['학기', '과목','수강 학점','이수 학점','전공 유무'])


def All_seme():
    global all_semester, year, semester
    year, semester = input('학년, 학기 : ').split()     #학기 계산
    year, semester  = int(year),int(semester)
    
    if semester%2 == 0 :
        all_semester = year * semester
        return print(all_semester,'학기 (총)')
       
    else :
        all_semester = (year * year) -1
        return print(all_semester,'학기 (총)')
    

for i in range(all_semester):
    num = int(input('과목 수강 수 '))
    for i in range(num):
        a = input("학기, 과목, 수강 학점, 이수 학점, 전공 유무 : ").split()
        df = pd.DataFrame({'학기' : [a[0]], '과목' : [a[1]], '수강 학점' : [a[2]],
                           '이수 학점' : [a[3]],'전공 유무' : [a[-1]]})
        
        All_Grade = All_Grade.append(df, ignore_index = True)
    
"-------------------------------------------------- 분석 (편의를 위한 엑셀 데이터 가져오기)"
#파일 보기좋게 정리, 결측값 0채우기
grade = pd.read_excel('D:\파일\학교\성적.xlsx')
grade.columns = ['학년','학기', '전공 유무', '과목','수강 학점','이수 학점','석차']
grade.isnull().sum()
grade = grade.fillna(0)
grade = grade.drop([0])
grade = grade.drop(['석차'], axis = 1)
grade['수강 학점'] = grade['수강 학점'].astype(int)

#학점 숫자로 바꾸기

def numbers():
    global a 
    a = []
    for i in grade['이수 학점']:
        if i == 'A+' :
            a.append(4.5)
        elif i == 'A' :
            a.append(4.0)
        elif i == 'B+' :
            a.append(3.5)
        elif i == 'B' :
            a.append(3.0)
        elif i == 'C+' :
            a.append(2.5)
        elif i == 'C' :
            a.append(2.0)
        elif i == 'D+' :
            a.append(1.5)
        elif i == 'D' :
            a.append(1.0)
        elif i == 'F' :
            a.append(0.0)
        else :
            a.append(0.0)
        
grade = grade.assign(학점 = a)



#패논패 있을 때 학점 계산 다르게 하는거... 


#------------------------------------------

'''   
y_s : 원하는 학년의 학기. 학년 데이터프레임 만들기
mean_grade : 원하는 데이터프레임 넣으면 해당 프레임 학점 평균
mean_major : 원하는 데이터프레임 넣으면 해당 프레임 전공, 교양학점 평균

'''
#이수 학점

def y_s(y,s): #한 학기, 한 학년 데이터프레임
    global grade_y, grade_ys
    grade_y = grade['학년'] == y
    grade_y = grade[grade_y]
    grade_ys = grade_y['학기'] == s
    grade_ys = grade_y[grade_ys]
    return grade_ys

def mean_grade (data): 
    mean_g = data['학점'].mean()
    return mean_g
    
def mean_major(data): 
    mean_m = data.groupby(['전공 유무']).mean()
    return mean_m['학점']


#수강 학점

def sum_grade(data):
    sum_g = data['수강 학점'].sum()
    return sum_g

def sum_major(data):
    sum_m = data.groupby(['전공 유무']).sum()
    return sum_m['수강 학점']


