'''
8种九九乘法表的实现
'''

# while循环的四种方式

# 从1开始，第一列，第一个数字从1到9；第二列，第一个数字从2到9；以此类推，每列相同的第一个数字置于同一行
first_num = 1
while first_num < 10:
    second_num = 1
    while second_num <= first_num:
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
        second_num = second_num + 1
    first_num = first_num +1
    print('')
print('='*80)

# 从9开始， 第一列，第一个数字从9到1；第二列，第一个数字从8到1；一次类推，每列相同的第一个数字置于同一行
first_num = 9
while first_num >= 1:
    second_num = 1
    while second_num <= first_num:
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
        second_num = second_num + 1
    print('')
    first_num = first_num - 1
print('=' * 80)


# 第一种方式的反方向输出
first_num = 1
while first_num < 10:
    second_num = 1
    print(' ' * (72 - first_num * 8), end='')
    while second_num <= first_num:
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
        second_num = second_num + 1
    first_num = first_num +1
    print('')
print('='*80)

# 第二种方式的反方向输出
first_num = 9
while first_num >= 1:
    second_num = 1
    print(' ' * (72 - first_num * 8), end='')
    while second_num <= first_num:
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
        second_num = second_num + 1
    print('')
    first_num = first_num - 1
print('=' * 80)

# for循环的四种方式

# 方式1
for first_num in range(1,10):
    for second_num in range(1,first_num+1):
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
    print('')
print('='*80)

# 方式2
for first_num in range(9,0,-1):
    for second_num in range(first_num,0,-1):
        print('{}*{}={:<3}'.format(first_num, second_num, first_num * second_num), end=' ')
    print('')
print('=' * 80)

# 方式3
for first_num in range(1,10):
    print(' ' * (72 - first_num * 8), end='')
    for second_num in range(1,first_num+1):
        print('{}*{}={:<3}'.format(first_num,second_num,first_num*second_num),end=' ')
    print('')
print('='*80)

# 方式4
for first_num in range(9,0,-1):
    print(' ' * (72 - first_num * 8), end='')
    for second_num in range(first_num,0,-1):
        print('{}*{}={:<3}'.format(first_num, second_num, first_num * second_num), end=' ')
    print('')
print('=' * 80)