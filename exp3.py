a = '''n = int(input('enter a number'))
d = dict()
for x in range(1,n+1):
    d[x] = x*x
print('The square number dictionary are: ',d)
print('The sum of elements in dictionary: ',sum(d.values()))
y = int(input('Enter the number to be searched: '))
if y in d:
    print('the number is present in dictionary')
else:
    print('The number is absent')


n = int(input('Enter no. of days: '))
y = n / 365
w = n % 365 / 7
d = n % 365 % 7
print('the no. of years:',int(y),'\nno. of weeks:',int(w),'\nno. of remaning days:\n',int(d))


n = int(input('Enter the length of series: '))
pre_no = 0
curr_no = 1
count = 2
print(pre_no)
print(curr_no)
while count<n:
    next_no = curr_no + pre_no
    pre_no = curr_no
    curr_no = next_no
    count += 1
    print(next_no)
print('The series is terminated')
'''


