# 满100打8折，满150打5折，坐班车是6块钱，坐地铁是4块钱

# 地铁和班车都用公交卡  共花费：379.2元
def by_buscar(subway = 4,bus = 6):
    sum = 0;
    for b in range(1,45):
        if sum < 100:
            sum_day = subway + bus
            sum = sum_day + sum
            print("第" + str(b/2) + "天花费: "+str(sum) + "元\n")
            continue
        if sum >=100 and sum < 150:
            sum_day = subway * 0.8 + bus
            sum = sum_day + sum
            print("第" + str(b/2) + "天花费" + str(sum) + "元  打8折 \n")
            continue
        if sum >=150:
            sum_day = subway * 0.5 + bus
            sum = sum_day + sum
            print("第" + str(b / 2) + "天花费" + str(sum) + "元 打5折\n")
            continue
# by_buscar()

# 地铁用公交卡，班车用学生卡  共花费：289.2
def by_bus_studen(buscar = 4,studencar = 3):
    sum_buscar = 0;
    sum_studencar = 0;
    sum_totle = 0;
    for b in range(1,45):
        if sum_buscar < 100:
            sum_buscar = buscar + sum_buscar
            sum_studencar = studencar + sum_studencar
            sum_totle = sum_studencar + sum_buscar
            print("第" + str(b / 2) + "天花费: " + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar)+"\n")
            continue
        if sum_buscar >= 100 and sum_buscar < 150:
            sum_buscar = buscar * 0.8 + sum_buscar
            sum_studencar = studencar + sum_studencar
            sum_totle = sum_studencar + sum_buscar
            print("第" + str(b / 2) + "天花费" + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar) + " 打8折\n")
            continue
        if sum_buscar >= 150:
            sum_buscar = buscar * 0.5 + sum_buscar
            sum_studencar = studencar + sum_studencar
            sum_totle = sum_studencar + sum_buscar
            print("第" + str(b / 2) + "天花费" + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar)+" 打5折\n")
            continue
# by_bus_studen()

#公交卡超过150后，班车用学生卡  共花费：295.2
def by_subway_bus(subway=4, studencar=3, buscar=6):
    sum_buscar = 0;
    sum_studen = 0;
    sum_totle = 0;
    for b in range(1, 45):
        if sum_buscar < 100:
            sum_buscar = buscar + subway + sum_buscar
            # sum_totle = studencar + buscar + sum_totle
            print("第" + str(b / 2) + "天花费: " + str(sum_buscar) + "元   公交卡花费: " + str(sum_buscar) + "\n")
            continue
        if sum_buscar >= 100 and sum_buscar < 150:
            sum_buscar = subway * 0.8 + buscar + sum_buscar
            # sum_totle = studencar + buscar * 0.8 + sum_totle
            print("第" + str(b / 2) + "天花费" + str(sum_buscar) + "元   公交卡花费: " + str(sum_buscar) + " 打8折\n")
            continue
        if sum_buscar >= 150:
            sum_buscar = subway * 0.5 + sum_buscar
            sum_studen = studencar + sum_studen
            sum_day = sum_studen + subway * 0.5
            sum_totle = sum_buscar + sum_studen
            print("第" + str(b / 2) + "天花费" + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar) + " 打5折\n")
            continue
# by_subway_bus()

# 公交卡超过100后，班车用学生卡  共花费：289.2
def by_subway_bus_studen(subway=4, studencar=3, buscar=6):
    sum_buscar = 0;
    sum_studencar = 0;
    sum_totle = 0;
    for b in range(1, 45):
        if sum_buscar < 100:
            sum_buscar = buscar + subway + sum_buscar
            # sum_totle = studencar + buscar + sum_totle
            print("第" + str(b / 2) + "天花费: " + str(sum_buscar) + "元   公交卡花费: " + str(sum_buscar) + "\n")
            continue
        if sum_buscar >= 100 and sum_buscar < 150:
            sum_buscar = subway * 0.8 + sum_buscar
            sum_studencar = studencar + sum_studencar
            sum_day = subway * 0.8 + studencar
            sum_totle = sum_studencar + sum_buscar
            print("第" + str(b / 2) + "天花费" + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar) + " 打8折")
            print("当日花费： " + str(sum_day)+"\n")
            continue
        if sum_buscar >= 150:
            sum_buscar = subway * 0.5 + sum_buscar
            sum_studencar = studencar +sum_studencar
            sum_day = studencar + subway * 0.5
            sum_totle = sum_buscar + sum_studencar
            print("第" + str(b / 2) + "天花费" + str(sum_totle) + "元   公交卡花费: " + str(sum_buscar) + " 打5折")
            print("当日花费： " + str(sum_day)+"\n")
            continue
# by_subway_bus_studen()

#地铁和公交都用学生卡  共花费: 259.60
def by_studencar(subway=4, bus=3):
    sum = 0;
    for b in range(1, 45):
        if sum < 100:
            sum = subway + bus + sum
            print("第" + str(b / 2) + "天花费: " + str(sum) + "元\n")
            continue
        if sum >= 100 and sum < 150:
            sum = subway * 0.8 + bus + sum
            print("第" + str(b / 2) + "天花费" + str(sum) + "元  打8折 \n")
            continue
        if sum >= 150:
            sum = subway * 0.5 + bus + sum
            print("第" + str(b / 2) + "天花费" + str(sum) + "元 打5折\n")
            continue
by_studencar()
