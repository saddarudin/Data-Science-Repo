"""
Write a program that prints following shape

*
**
***
****
*****

"""

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')


