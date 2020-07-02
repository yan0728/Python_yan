# 需要在python3上执行
import random
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
                i = 1
                while i > 0:
                    game(capital = capital)
        else:
            print("***下注资金只能是正整数，请您重新下注***\n")
            game(capital = capital)
    else:
        print("***选择大小时仅允许输入 “大” 或 “小”，请重新下注!***\n")
        game(capital = capital)
# game()
def shoot():
    shoot_orientation = random.choice(['左','中','右'])
    print("<<<<<<<<<游戏开始>>>>>>>>>>>")
    player = input("输入您要射门的方向: ")
    if shoot_orientation == player:
        print("您的球被守门员扑出,请开始下一局\n")
        shoot()
    elif player != '左'and player != '中'and player != '右':
        print("您输入的有误，请重新输入\n")
        shoot()
    else:
        print("您的球射入了门框，守门员扑球方向为---%s\n"%shoot_orientation)
        again = input("请确定你是否继续？继续请输入1，否则请输入2： ")
        if again == str(1):
            shoot()
        else:
            quit()
# shoot()

f = open('data.txt','w')


