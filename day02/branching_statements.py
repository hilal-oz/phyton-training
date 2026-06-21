for i in range(1,6):
    print(i) #1 2 3 4 5
    if i==3:
        break #1 2 3
print('-------------')
for i in range(1, 6):
    if i == 3 or i==4:
        continue
    print(i)
print('-------------')

for i in range(1,6):
    if i==3 or i==4:
        pass
    print(i)# 1 2 3 4 5
