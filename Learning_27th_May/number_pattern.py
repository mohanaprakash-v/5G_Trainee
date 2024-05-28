print("---------------------------------")
n=5
for i in range(n):
    for j in range(i+1): 
        print(i*2, end=' ')
    print()

#--Pattern 1--
print("---------------------------------")
n=5
for i in range(n):
    for j in range(i+1): 
        if i%2==0:
            print('1', end=' ')
        else:
            print('2', end=' ')
    print()

#--Pattern 2--
print("---------------------------------")
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print(p,end=' ')
    for j in range(i+1):
        print(p, end=' ')
    p+=1
    print()
p=5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n):
        print(p, end=' ')
    for j in range(i,n):
        print(p, end=' ')
    p+=1
    print()

#--Pattern 3--
print("---------------------------------")
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print(p,end=' ')
    for j in range(i+1):
        print(p, end=' ')
    p+=1
    print()
p = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n):
        print(p, end=' ')
    for j in range(i,n):
        print(p, end=' ')
    p-=1
    print()

#--Pattern 4--
print("---------------------------------")
n=5
for i in range(1,n+1):
    for j in range(1,i+1): 
        print(j, end=' ')
    print()

#--Pattern 5--
print("---------------------------------")
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n+1):
        print(p, end=' ')
        p+=1
    print()

#--Pattern 6--
print("---------------------------------")
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print(p,end=' ')
        p+=1
    for j in range(i+1):
        print(p, end=' ')
        p+=1
    for j in range(i,n):
        print(' ', end=' ')
    print()

#--Pattern 6--
print("-------------BUTTERFLY NUMBER PATTERN--------------------")
n=5
for i in range(n):
    for j in range(1,i+2):
        print(j, end=' ')
    for j in range(i,n-1):
        print(' ', end=' ')
    for j in range(i,n-1):
        print(' ', end=' ')
    for j in range(1,i+2):
        print(j, end=' ')
    print()

for i in range(n):
    p=1
    for j in range(i,n-1):
        print(p, end=' ')
        p+=1
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n-1):
        print(p, end=' ')
    p-=1
    print()

