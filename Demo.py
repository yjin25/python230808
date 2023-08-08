# Demo_Slice.py
strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

print(strA[0:6])
print(strB[0:4])

print(strA[:6])
print(strB[:4])
print(strA[-3:])
print(strB[-3:])

strC = """다중라인을
저장해서
작업하는 경우
"""
print(strC)

#대소문자 구분
friend = 5
Friend = 6
print(friend)
print(Friend)

# 리스트 형식
colors = ["red", "blue", "green"]
print( type(colors) )
colors.append("white")
print(colors)
colors.insert(1, "pink")
print(colors)

colors += ["red"]
colors == "red"

print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors)

#정순으로 정렬
colors.sort()
print(colors)
colors.reverse()
print(colors)

print("===set형식===")
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Demo_Tuple

print("=======tuple 형식========")
tp = (1,2,3)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("kim","김유신"))

# 함수 정의
def calc(a,b):
    return a+b, a*b
#함수를 호출(디버깅할 때 중단점-Break Point)
result = calc(3,4)
print(result)
#*를 붙이면 Tuple 형식이라는 뜻
args = (5,6)
print(calc(*args))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b) # list인 b를 tuple화 시켜서 c에 대입
print(c)


print("=========dict형식==========")
fruits = {"apple":"red", "banana":"yellow"}
print(fruits["apple"])
fruits["kiwi"] = "green"
print(fruits)
for item in fruits.items():
    print(item)

for k,v in fruits.items():
    print(k, v)

print("----- 값만 출력 -----")
for v in fruits.values():
    print(v)
print("----- 키만 출력 -----")
for k in fruits.keys():
    print(k)