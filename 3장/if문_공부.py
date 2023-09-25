money = True
if money:
    print("주식을 사라")
else:
    print("노동을 해라")


돈미새 = False
if 돈미새:
    print("머리에 돈 생각뿐이다")
else:
    print("~머리에 돈 생각뿐이다")


money = 1500
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


card = True
money_in_card = 1300
if money_in_card >= 1500 and card:
    print("마이쮸를 사 먹어라")
else:
    print("마이쮸를 사지 말아라")


Rainy = True
if not Rainy:
    print("우산을 사지 마라")
else:
    print("우산을 사라")


Pocket = ["money", "candy", "phone"]
if 'money' in Pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


Pocket = ["money", "candy", "phone"]
if 'money' in Pocket:
    pass
else:
    print("카드를 꺼내라")


Pocket = ["money", "candy", "phone"]
if 'money' in Pocket: pass
else: print("카드를 꺼내라")


Pocket = ["money", "candy", "phone"]
card = True
if 'money' in Pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")


Pocket = ["money", "candy", "phone"]
card = True
if 'money' in Pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


score = 60
message = "good" if score >= 70 else "failure"
print(message)


대학원 = int(input("합격 여부는? 합격했다면 1, 불합했다면 0: "))
if 대학원 == 1:print("합격 ㅊㅊ")
else: pass