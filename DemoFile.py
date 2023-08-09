# DemoFile.py
# 파일 쓰기

f = open("C:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일 읽기(r => raw string natation)
f = open(r"C:\work\demo.txt", "rt", encoding="utf-8")
print(f.read())

print("=====readline()=====")
f.seek(0)
# 코드에서 보정
print(f.readline(), end="")
print(f.readline(), end="")
print("=====readlines()=====")
f.seek(0)
result = f.readlines()
print(result)
for item in result:
    print(item, end="")

f.close()



