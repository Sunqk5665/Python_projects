print('Hello world')  # O(1)
 
 
# O(1)
print('Hello World')
print('Hello Python')
print('Hello Algorithm')
 
 
for i in range(n):  # O(n)
    print('Hello world')
 
 
for i in range(n):  # O(n^2)
    for j in range(n):
        print('Hello world')
 
 
for i in range(n):  # O(n^2)
    print('Hello World')
    for j in range(n):
        print('Hello World')
 
 
for i in range(n):  # O(n^2)
    for j in range(i):
        print('Hello World')
 
 
for i in range(n):
    for j in range(n):
        for k in range(n):
            print('Hello World')  # O(n^3)
