N = int(input())

m2 = 0
m3 = 0
m4 = 0
m5 = 0

values = input().split(' ')
values_correctly = values[:N]
for i in range(N):
    values_correctly[i] = int(values_correctly[i])
    if(values_correctly[i] % 2 ==0):
        m2+=1
    if(values_correctly[i] % 3 ==0):
        m3+=1
    if(values_correctly[i] % 4 ==0):
        m4+=1
    if(values_correctly[i] % 5 ==0):
        m5+=1

print('{0} Multiplo(s) de 2'.format(m2))
print('{0} Multiplo(s) de 3'.format(m3))
print('{0} Multiplo(s) de 4'.format(m4))
print('{0} Multiplo(s) de 5'.format(m5))
