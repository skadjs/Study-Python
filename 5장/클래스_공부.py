class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.sub(3))
print(cal2.sub(7))


# class 안에 구현된 함수는 다른 말로 "method(매서드)"라 부름.


class FourCal:
    pass         #아무것도 수행 않는 문법, 임시로 코드 작성 시 주로 사용
a = FourCal()


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)
b = FourCal(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())


# class 상속
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


# class 상속 후 변경 - 기능 추가
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())
print(a.add())


# class 상속 후 변경 - 기능 수정
# 매서드 오버라이딩: 부모 클래스의 메서드를 같은 이름으로 다시 만드는 것
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)
print(a.div())


# 클래스변수
class Family:
    lastname = "김"

a = Family()
print(a.lastname)


class Family:
    lastname = "김"

Family.lastname = "박"

a = Family()
print(a.lastname)