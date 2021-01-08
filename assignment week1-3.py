'''
自动存取款机系统，功能如下：
1. 通过账号、密码登录系统，显示账户信息；
2. 取款；
3. 存款；
4. 查询余额；
5. 退出系统
'''


# 设置系统初始账户信息
acc_info = [
    {'username': 'ZS', 'pin': 123, 'balance': 1000},
    {'username': 'LS', 'pin': 321, 'balance': 200},
    {'username': 'WE', 'pin': 456, 'balance': 500}
]

i = 0  # 定义全局变量
# 登录判断函数
def sign_in():
    global i
    user = input('用户名：')
    for i in range(len(acc_info)):
        curr_info_name = acc_info[i].get('username')
        if curr_info_name == user:
            psw = input('密 码：')
            if acc_info[i].get('pin') == int(psw):
                sign_in_interface()
            else:
                print('密码错误')
                break  # 结束遍历账户信息列表
        continue  # 继续遍历账户信息列表
    return i


# 存款函数
def fun_deposit():
    amount_cash = input('请输入您的存款金额：')
    pre_balance = acc_info[i].get('balance')
    balance_bank = int(amount_cash) + pre_balance
    return balance_bank


# 取款函数
def fun_withdro():
    amount_cash = input('请输入您的取款金额：')
    pre_balance = acc_info[i].get('balance')
    balance_bank = pre_balance - int(amount_cash)
    return balance_bank


# 查询函数
def fun_check():
    print('用 户 名：', acc_info[i].get('username'))
    print('密   码：', acc_info[i].get('pin'))
    print('存款余额：', acc_info[i].get('balance'))

# 登录后界面显示函数
def sign_in_interface():
    print('\n'*3)
    # 系统界面标题
    print(' ' * 23, '登陆成功', ' ' * 23)
    print('')
    print('=' * 21, '自动存取款系统', '=' * 21)
    print('-' * 55)
    print('')
    print('{:<8}{:<8}{:>10}{:>15}'.format('|', '1. 存款', '|', '2. 取款'))
    print('-' * 55)
    print('{:<8}{:<8}{:>9}{:>15}'.format('|', '3. 查询余额', '|', '4. 退出'))
    print('')
    ch_item = input('您希望的操作是：')
    if int(ch_item) == 1:
        balance_new = fun_deposit()
        print(balance_new)
        sign_in_interface()
    elif int(ch_item) == 2:
        balance_new = fun_withdro()
        print(balance_new)
        sign_in_interface()
    elif int(ch_item) == 3:
        fun_check()
        sign_in_interface()
    elif int(ch_item) == 4:
        print('下次再见！')


# 登录选项
print('-' * 55)
print(' '*17, '登录后才能使用系统功能')
print('')
print(' '*13, '1. 登录', ' '*10, '2. 放弃登录')
print('-'*55)
print('')
goto = input('您的选择是：')
if int(goto) == 1:
    sign_in()
else:
    print('再见！')
