treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니니다.")


time = 0
while time < 20:
    time = time + 1
    print("이재명 단식 %d일째입니다." % time)
    if time == 20:
        print("단식 끝났습니다.")


coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


milk = 3
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("우유를 줍니다.")
        milk = milk - 1
        print("남은 우유의 양은 %d개입니다." % milk)
    elif money > 300:
        print("거스름돈 %d를 주고 우유를 줍니다." %(money - 300))
        milk = milk - 1
        print("남은 우유의 양은 %d개입니다." % milk)
    else:
        print("돈을 다시 돌려주고 우유를 주지 않습니다.")
        print("남은 우유의 양은 %d개입니다." % milk)
    if milk == 0:
        print("우유가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


while True:
    print("Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")