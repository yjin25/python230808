# DemoFormat.py

for x in range(1,6):
    print(x,"*", "=", x*x)

print("=====오른쪽 정렬=====")
for x in range(1,6):
    print(x,"*", "=", str(x*x).rjust(3)) #rightjust

print("=====왼쪽 정렬=====")
for x in range(1,6):
    print(x,"*", "=", str(x*x).zfill(5)) #zerofill

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(150000000))