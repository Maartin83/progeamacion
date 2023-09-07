n=12
v1=1
v2=1
print('0')
print(v1)
print(v2)

for x in range(n):
    total =v1+v2
    v2=v1
    v1=total
    print(total)
