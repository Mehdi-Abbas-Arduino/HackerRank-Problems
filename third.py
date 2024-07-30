# for i in zip([1,2,3,4,5,6],'Hacker'):
#     print(i)

N,X = map(int,input().split())
marks = []

for i in range(X):
    marks.append(map(float,input().split()))
    
for studentScores in zip(*marks):
    print (sum(studentScores)/len(studentScores))