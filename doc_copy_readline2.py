# 정규표현식 사용
import re 

# 파일 읽기,쓰기
f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='EUC-KR')

# 많은 라인의 파일이면 
# 한번에 한줄씩 읽어서 처리한다.  
# 파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): # EOF가 아니면 계속
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








