import random

def getLOTTO() :
    LOTTO = []
    for i in range(0,6) :
        LOTTO.append(i)
        LOTTO[i] = random.randrange(1, 46)
        if i == 6 : break 
        LOTTO.sort()
    return LOTTO
    
print("로또 추첨을 시작합니다.\n")
Num = []
Num = getLOTTO()
print("당첨 번호는 : ", end = " ")
for i in range(0, 6) :
    print("%d " % Num[i], end = " ")