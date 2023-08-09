# 우리는 텍스트에서 무언가를 찾는 특별한 도구를 가져와요.
import re

# 우리는 "find_emails"라는 새로운 특별한 능력을 만들어볼게요.
def find_emails(text):
    # 우리는 이메일 주소를 찾는 규칙들을 만들 거에요, 마치 특별한 패턴을 찾아보는 것처럼요.
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # 우리는 우리의 특별한 능력을 사용해서 텍스트에서 우리가 만든 규칙과 일치하는 것들을 찾아볼 거에요.
    matches = re.finditer(pattern, text, re.IGNORECASE)

    # 우리는 찾은 각각의 것을 확인하고, 일치하는 경우에는 모두에게 보여줄 거에요.
    for match in matches:
        print(match.group())

# 이것은 특별한 이메일 주소를 찾고자 하는 이야기에요.
text = """
도움이 필요하면 support@example.com 으로 연락해주세요.
추가 정보를 위해 info@mywebsite.org 로 연락할 수도 있어요.
"""

# 우리는 우리의 특별한 능력을 사용해서 이야기에서 이메일 주소를 찾아서 모두에게 보여줄 거에요.
find_emails(text)