# Enter your code here. Read input from STDIN. Print output to STDOUT

s1=input().split()
k=int(s1[0])
m=int(s1[1])

M=[[0]]*7

for i in range(k):
    s1=input().split()
    l=[]
    for s in range(len(s1)):
        if s!=0:
            l.append(int(s1[s]))
    M[i]=l

s=0
for x1 in M[0]:
    for x2 in M[1]:
        for x3 in M[2]:
            for x4 in M[3]:
                for x5 in M[4]:
                    for x6 in M[5]:
                        for x7 in M[6]:
                            x=(x1*x1+x2*x2+x3*x3+x4*x4+x5*x5+x6*x6+x7*x7)%m
                            if s<x:
                                s=x


print(s)

