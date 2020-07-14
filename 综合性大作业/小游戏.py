# 需要在python3上执行
import random
from login import account_login
# import Test

def game (capital = 1000):
    point1 = random.randrange(1,7)
    point2 = random.randrange(1,7)
    point3 = random.randrange(1,7)
    print("<<<<<<<<<< 游戏开始 >>>>>>>>>>")
    result = point3 + point2 + point1
    大 = range(11,19)
    小 = range(3,11)
    print("请选择大小，如果选择“大”请输入“大”，否则输入“小”")
    cai = input("大 or 小: ")
    if cai == '大' or cai == '小':
        print("您的本金有",capital)
        xiaZhu = input("您想下注多少钱?（请输入正整数，并且不能超过本金）: ")
        if xiaZhu.isdigit():
            if abs(float(xiaZhu)) > capital:
                print("***您下的注金不能高过您的本金，您的本金还有:",str(capital)+"元，请重新下注！\n")
                game(capital = capital)
            else:
                print('<<<<<<<<< 买定离手，开始摇筛子了!!! >>>>>>>>>')
                if cai == '大':
                    if result in 大:
                        print("点数是"+ str([point3, point2, point1]),"You Win!")
                        capital = capital + abs(float(xiaZhu))
                        print('您赢得了'+ str(abs(float(xiaZhu)))+'元'+'，您现在有'+ str(capital)+ '元\n')
                    else:
                        print("摇得的点数是"+ str([point3, point2, point1]),"You Lose!")
                        capital = capital - abs(abs(float(xiaZhu)))
                        print('您输了' + str(xiaZhu) + '元' + '，您现在有' + str(capital) + '元\n')
                else:
                    cai == '小'
                    if result in 小:
                        print("点数是"+ str([point3, point2, point1]),"You Win")
                        capital = capital + abs(abs(float(xiaZhu)))
                        print('您赢得了' + str(abs(float(xiaZhu))) + '元' + '，您现在有' + str(capital) + '元\n')
                    else:
                        print("点数是"+ str([point3, point2, point1]),"You Lose!")
                        capital = capital - abs(float(xiaZhu))
                        print('您输了' + str(abs(float(xiaZhu))) + '元' + '，您现在有' + str(capital) + '元\n')
            if capital <=0:
                print("*** 您的资金已经用光,GAME OVER!!! ***")
                quit()
            else:
                # i = 1
                while True:
                    game(capital = capital)
        else:
            print("***下注资金只能是正整数，请您重新下注***\n")
            game(capital = capital)
    else:
        print("***选择大小时仅允许输入 “大” 或 “小”，请重新下注!***\n")
        game(capital = capital)

account_login()
game()
