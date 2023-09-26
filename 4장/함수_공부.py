#입력값 ㅇ, 리턴값 ㅇ
def add(a, b):
    return a + b          #함수 정의
A = add(3, 4)
print(A)                  #함수 사용


#입력값 x, 리턴값 ㅇ
def say():
    return 'Hi'           #함수 정의
a = say()
print(a)                  #함수 사용

#근데 Hi를 출력하고 싶은 거면 걍 print("Hi") 한 줄 쓰는 게 낫지 않나?


#입력값 ㅇ, 리턴값 x
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))    #함수 정의
add(3, 4)                                            #함수 사용


#입력값 x, 리턴값 x
def say():
    print('Hi')                #함수 정의
say()                          #함수 사용


def sub(a, b):
    return a - b
result = sub(a=7, b=3)         #매개변수 지정
print(result)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


#키워드 매개변수-딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)


def add_and_mul(a, b):
    return a+b, a*b
result = add_and_mul(3, 4)
print(result)


def add_and_mul(a, b):
    return a+b, a*b
result1, result2 = add_and_mul(3, 4)
print(result1, result2)

#함수는 return문을 만나는 순간 리턴값을 돌려준 뒤 함수를 빠져나간다.


#리턴값이 없는 함수에서 return으로 함수 빠져나가기
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)
say_nick('야호')
say_nick('바보')


def say_myself(name, age, man=True):  #man=True << 매개변수 초기값 설정
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("김애용", 23)               #man은 초기값 True를 가짐
say_myself("때껄룩", 24, False)


#초기값이 있는 매개변수는 초기값이 없는 매개변수의 뒤에 와야 한다.


#함수 안의 매개변수는 함수 안에서만 사용된다.
a = 1
def vartest(a):
    a = a +1
vartest(a)
print(a)


#함수 안에서 함수 밖의 변수 변경하기
#return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)


#global 명령어 사용하기(권하진 않음)
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)


#람다는 나중에