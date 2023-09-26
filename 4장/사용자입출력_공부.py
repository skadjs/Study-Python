number = input("숫자를 입력하세요: ")
print(number)
#input에 입력되는 모든 것은 문자열 취급
#input은 시간복잡도 측면에서 불리합니다...


a = 123
print(a)


a = "Python"
print(a)


a = [1, 2, 3]
print(a)


print("Life" "is" "too short")
print("Life", "is", "too short")      #쉼표로 문자열 띄어쓰기


for i in range(10):
    print(i, end = ' ')
#end 매개변수의 초기값은 '\n(줄바꿈 문자)'
#얘를 다른 걸로 바꾸는 게 end = ''