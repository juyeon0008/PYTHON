
"""
거북이 프로젝트 - 학점 계산기 다시 만들기 아이디어
"""

sub = ['사고와 표현','대학영어 1','창의적 문제해결','세계화와 국제관계','경제학원론 1','통계학개론 1','전진탐']
credit = [3,3,3,3,3,3,1]
grade = [4.5,4.5,4,3,4.5,4,'P']
major = [0,0,0,0,1,1,1]


semester_1 = [[sub, credit, grade, major] for sub, credit, grade, major in zip(sub, credit, grade, major)]


-------------------------------

#학기 안에 과목, 한 학기 계산
class Subject (object):
    def __init__(self, sub, credit, grade, major):
        self.sub = sub
        self.credit = credit
        self.grade = grade
        self.major = major
        

print("과목", "이수학점", "성적","전공 여부")

for i in semesters :
    print(i)


print(semester)
semester 라는 리스트에서 계산이 돌아간다


semester = [['통계학개론 1',3,4.0,1],
            ['경제학원론 1',3,4.5,1]]

seme = [[a,b]for a,b in zip(semester[0], semester[1])]





num = int(input('강의 수강 수 '))                  #학기, 과목 입력, 각각 분리
for i in range(num):
    subject = input('강의명, 수강학점, 취득학점, 전공여부 ').split()
    semesters.append(subject)
    



sub_1 = ['사고와 표현',3,4.5,0]
sub_2 = ['대학영어 1',3,4.5,0]
sub_3 = ['창의적 문제해결',3,4,0]
sub_4 = ['세계화와 국제관계',3,3,0]
sub_5 = ['경제학원론 1',3,4.5,1]
sub_6 = ['통계학개론 1',3,4.0,1]
sub_7 = ['전진탐',1,4.5,1]


semesters = [[sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7] for sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7 in zip(sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7)]

semesters[0]
sum(semesters[1])

def grade_mean ():
    return sum(semesters[2])/len(semesters[2])

def major_mean():

------------------------------------

"""
거북이 프로젝트 - 학점 계산기 ( 한 학기 )
"""

class Subject (object):
    def __init__(self, seme, sub, cre, gra, maj):
        self.seme = seme
        self.sub = sub
        self.cre = cre
        self.gra = gra
        self.maj = maj
        
    def All_cre (self):
        all_cre = 0
        for i in range(len(Univ)):
            all_cre += Univ[i][2]
            return all_cre
        
        


semesters = [Subject(1,'사고와 표현',3,4.5,0),
             Subject(1,'대학영어 1',3,4.5,0),
             Subject(1,'창의적 문제해결',3,4,0),
             Subject(1,'세계화와 국제관계',3,3,0),
             Subject(1,'경제학원론 1',3,4.5,1),
             Subject(1,'통계학개론 1',3,4.0,1),
             Subject(1,'전진탐',1,4.5,1)]


all_cre = 0
for i in range(len(semesters)):
    all_cre += semesters[i][2]
    print( all_cre)


























