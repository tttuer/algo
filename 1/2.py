"""
[문제: 팰린드롬 확인하기]

주어진 문자열이 **팰린드롬(앞으로 읽으나 뒤로 읽으나 같은 문장)**인지 확인하는 함수를 작성하세요. 단, 알파벳과 숫자만 대상으로 하며 대소문자는 구분하지 않습니다.

입력: s = "A man, a plan, a canal: Panama"

출력: True (공백과 특수문자를 제외하고 합치면 'amanaplanacanalpanama'가 되어 대칭임)
"""

import sys

input = sys.stdin.readline().strip()

fixed_input = [word.lower() for word in input if word.isalnum()]

left, right = 0, len(fixed_input) - 1

answer = True
for i in range(0, len(fixed_input)//2):
    if fixed_input[left+i] != fixed_input[right-i]:
        answer = False
        break

print(answer)

