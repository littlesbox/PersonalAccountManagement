class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def f(a):
    a.age=0

wangcai = dog("wangcai", 3)
print(wangcai.age)
f(wangcai)
print(wangcai.age)