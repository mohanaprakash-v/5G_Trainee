#----PATTERN PROGRAMMING------#

#--BOX PATTERN--
print("BOX PATTERN")
n=5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

#--INCREASING TRIANGLE--
print("INCREASING TRIANGLE PATTERN")
n=5
for i in range(n):
    for j in range(i+1): 
        print('*', end=' ')
    print()

#--DECREASING TRIANGLE--
print("DECREASING TRIANGLE PATTERN")
n=5
for i in range(n):
    for j in range(i,n):
        print('*', end=' ')
    print()

#--REVERSE DECREASE RIGHT TRIANGLE--
print("REVERSE DECREASE RIGHT TRIANGLE")
n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()

#--RIGHT TRIANGLE--
print("RIGHT TRIANGLE PATTERN")
n=5
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print() 

#--HILL TRIANGLE--
print("HILL TRIANGLE PATTERN")
n=5
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i,n):
        print(' ', end=' ')
    print()

#--REVERSE HILL TRIANGLE--
print("REVERSE HILL TRIANGLE PATTERN")
n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n):
        print('*', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()

#--DIAMOND PATTERN--
print("DIAMOND PATTERN")
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n):
        print('*', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()

#--X PATTERN--
print("X PATTERN")
n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1,n):
        print('*', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

#--BUTTERFLY PATTERN--
print("---BUTTERFLY PATTERN---")
n=5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i,n-1):
        print(' ', end=' ')
    for j in range(i,n-1):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i,n-1):
        print('*', end=' ')
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n-1):
        print('*', end=' ')
    print()