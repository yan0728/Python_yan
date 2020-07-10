# 登录操作
PassWord_list = []
Reset_pw = '*#*#'
def account_login():
    if PassWord_list == []:
       PassWord = input("请设置初始密码：")
       if PassWord.isalnum():
           PassWord_list.append(PassWord)
           account_login()
       else:
           print("密码只能是输入或字母，请重新输入")
           account_login()
    else:
        # print(PassWord_list)
        num = 3
        while num > 0:
            password = input('请输入您的登录密码： ')
            correct_password = password == PassWord_list[-1]
            reset_password = password == Reset_pw
            if correct_password:
                print("登录成功")
                quit()
            elif reset_password:
                new_password = input('请输入要重置的密码: ')
                if new_password.isalnum():
                     PassWord_list.append(new_password)
                else:
                    print("密码只能是输入或字母，请重新输入")
                    account_login()
                print('密码已经重置成功，请输入重置的密码登录')
                account_login()
            else:
                print("您输入的密码错误，请再次输入或输入'*#*#'重置密码")
                num = num -1
                print(num,'time left')
        print("输入次数过多")
account_login()