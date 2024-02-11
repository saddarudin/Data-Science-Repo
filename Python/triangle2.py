"""
Write a program that prints following shape

    *
   **
  ***
 ****
*****

"""
count = 1
for i in range(5, 0, -1):
    for j in range(i-1, 0, -1):
        print(' ', end='')
    for k in range(count):
        print('*', end='')
    count += 1
    print('')
