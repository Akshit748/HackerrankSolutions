if __name__ == '__main__':
    student_lst = []
for i in range(int(input())):
    name = input()
    score = float(input())

    student_lst.append([name,score])

sorted_score = sorted({item[1] for item in student_lst})
req = sorted(x for x, y in student_lst if y==sorted_score[1])
for name in req:
    print(name)
