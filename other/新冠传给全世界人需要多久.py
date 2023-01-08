# population = 8000000000
# r0 = 7
# date = 0
def TransmissionSpeed (population,r0,date):
    while r0 < population:
        date = date + 1
        r0 = r0 * 7
        print("第"+ str(date)+"天感染了"+ str(r0) +"人")

TransmissionSpeed(8000000000,1,0)