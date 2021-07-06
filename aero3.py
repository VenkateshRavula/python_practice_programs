from pprint import pprint

def compare_answers_and_key(answers, key, count=0):
    for i in range(len(key)):
        if key_list[i] == answers[i]:
            count = count+1
    return count


f_key = open('aero3_key.txt', 'r')
key_list = list(f_key.readline())
student_dict = {}
f_answers = open('aero3_answers.txt', 'r')
for student_detail in f_answers.readlines():
    student_marks = compare_answers_and_key(list(student_detail.split()[1]), key_list)
    print(">> student marks - {}".format(student_marks))
    student_dict[student_detail.split()[0]] = student_marks

sorted_marks = sorted(student_dict.values())
print(">> student marks list - {}".format(sorted_marks))

A_grade_cutoff = sorted_marks[-(len(sorted_marks)*3/10)]
B_grade_cutoff = sorted_marks[-(len(sorted_marks)*6/10)]
C_grade_cutoff = sorted_marks[-(len(sorted_marks)*8/10)]
D_grade_cutoff = sorted_marks[-(len(sorted_marks))]

Grade_dict = {}
for id, student_score in student_dict.items():
    if student_score >= A_grade_cutoff:
        Grade_dict[id] = 'A'
    elif A_grade_cutoff > student_score >= B_grade_cutoff:
        Grade_dict[id] = 'B'
    elif A_grade_cutoff > student_score >= C_grade_cutoff:
        Grade_dict[id] = 'C'
    else:
        Grade_dict[id] = 'D'

pprint(Grade_dict)
