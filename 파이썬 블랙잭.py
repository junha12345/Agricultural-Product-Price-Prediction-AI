import time #time.sleep를 쓰기위한 수단
from random import choice as rc #랜덤함수를 이용하기 위한 수단

def wincount(hcard): #wincount함수로 카드 중 에이스를 확인함
    Ace=hcard.count(11) #Ace에 경우 11로 따짐
    total=sum(hcard) #total은 hcard안에 들은 값들을 합함
    if total>21 and Ace>0 : #만약 total이 21을 넘긴경우 Ace를 11이 아닌 1로 취급
        while Ace>0 and total>21 :
            total-=10 #total값에 10을 뺌
            Ace-=1 #Ace카드의 횟수를 1개 뺌
    return total

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] #A, 2, 3, 4, 5, 6,7, 8, 9, 10, J, Q, K의 카드를 리스트로 표현
M=10 # 처음 칩 개수
C=0 # 건 칩의개수
bj=0 # 블랙잭 확인
play=str(input("블랙잭 게임을 플레이 하시겠습니까?(y/n) :"))
if (play=='y') :
    tutorial=str(input("게임 규칙설명을 들으시겠습니까?(y/n) :"))
    if(tutorial=='y') :
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n블랙잭은 카드 2~10과 A, J, Q, K의 카드를 각각 4장씩 총 52장의 카드로 구성된 카드팩을 가지고 딜러와 싸워서 이기는 게임입니다")
        time.sleep(2)
        print("플레이어는 처음 2장의 카드를 받고, 카드 수의 합이 21에 가장 가깝도록 만드는 것이 목표입니다.")
        time.sleep(2)
        print("딜러에 경우 17이상이 될때까지 카드를 계속해서 받고 만약 17을 넘으면 카드를 그만받고 플레이어와 대결합니다.")
        time.sleep(3)
    print("\n지금부터 블랙잭을 시작하겠습니다. 플레이어는 칩 10개를 가지고 칩 200개를 만들면 게임에서 승리합니다.")
    print("이길경우 건 칩의 2배를 받고, 질 경우에는 건 칩을 모두 잃습니다.")
    print("[Black Jack]으로 이길경우 건 칩의 3배를 받습니다.")
    time.sleep(2)
while True : #칩이 0개가 될때까지 무한반복
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----------------------------------------------------------------------\n현재 보유중인 칩 개수 :%d\n-----------------------------------------------------------------------" %M)
    bj=0
    print("셔플중")
    time.sleep(5)
    C=int(input("칩을 몇개 거시겠습니까? :"))
    if M==0 and C==777 :#제작자 치트키
        print("\n\n\n치트키 입력으로 칩 20개를 받습니다.\n\n\n")
        M=20
    while C>M : #보유한 칩보다 건 칩이 더 많을경우 무한반복
        print("건 칩이 보유한 칩보다 많습니다. 다시입력해 주세요!")
        C=int(input("칩을 몇개 거시겠습니까? :"))
    player = [] #플레이어의 리스트를 만듦
    player.append(rc(cards)) #플레이어의 리스트에 cards안에 든 리스트를 넣음
    player.append(rc(cards)) #위와 동일
    pbust=False #플레이어가 21을 넘었는지 확인
    cbust=False #딜러가 21을 넘었는지 확인
    while True :
        tp=wincount(player) #위 wincount(hcard)함수에 player리스트 값을 넣음 그 값이 플레이어 카드의 합이됨
        print("\n현재 플레이어는 %s의 카드를 가지고 있습니다. 합은 %d입니다.\n" % (player, tp))
        time.sleep(2)
        if tp>21 :#플레이어의 카드가 21을 넘을경우
            print("플레이어가 21을 넘겼습니다.")
            pbust=True
            break
        elif tp==21 :#플레이어가 블랙잭인 경우
            print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$BlacJack$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
            bj=1
            time.sleep(3)
            break
        else :#플레이어가 21보다 작을경우 카드를 받을것인지 안받을것인지 선택
            ch=str(input("카드를 받는다:hit       카드를 그만받는다:stop   ="))
            if (ch=='hit') :
                player.append(rc(cards))
            else :
                break
    while True :#딜러의 카드를 입력함
        computer = []
        computer.append(rc(cards))
        computer.append(rc(cards))
        while True :
            tc=wincount(computer)
            if tc<18 :
                computer.append(rc(cards))
            else :
                break
        print("\n현재 딜러는 %s의 카드를 가지고 있습니다. 합은 %d입니다." % (computer, tc))
        time.sleep(2)
        if tc>21 : #이 부분은 플레이어와 딜러의 카드 합을 가지고 승패를 가림 단, 플레이어의 카드가 21을 넘긴경우 무조건 패배
            print("\n딜러가 21을 넘겼습니다.")
            time.sleep(2)
            cbust=True
            if pbust == False :
                if bj==1 :
                    print("\n[Black Jack]으로 플레이어가 이겼습니다.")
                    M=M+2*C
                else :
                    print("\n플레이어가 이겼습니다.")
                    M=M+C
            else :
                print("\n딜러가 이겼습니다.")
                M=M-C
        elif tc>tp :
            time.sleep(2)
            print("\n딜러가 이겼습니다.")
            M=M-C
        elif tc==tp :
            print("\n무승부 입니다")
            time.sleep(2)
            if pbust == True :
                print("\n딜러가 이겼습니다.")
                M=M-C
            else :
                M=M
        elif tp>tc :
            time.sleep(2)
            if pbust == False :
                if bj==1 :
                    print("\n[Black Jack]으로 플레이어가 이겼습니다.")
                    M=M+2*C
                else :
                    print("플레이어가 이겼습니다.")
                    M=M+C
            elif pbust == True :
                print("\n딜러가 이겼습니다.")
                M=M-C
        break
    if (M==0) : #플레이어가 가진 칩이 0개가 된 경우 게임오버
        print("\n\n\n\n\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~\n~~~~~~~~~~Game Over~~~~~~~~~")
        continue
    elif (M==200) : #플레이어의 칩이 200개가 된 경우 게임에서 승리
        break
    time.sleep(2)
print("\n\n\n\n\n\n\n\n\n게임을 승리하셨습니다.\n\n\n\n\n\n\n\n\n")
time.sleep(3)
name=str(input("이름을 입력하세요. :"))
time.sleep(2)
print("\n\n\n\n\n%s님께서 목표를 달성하셨습니다." %name)
