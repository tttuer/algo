"""
[문제: 중복 문자 없는 가장 긴 부분 문자열]

문자열 s가 주어졌을 때, 중복된 문자가 없는 가장 긴 부분 문자열(substring)의 길이를 구하세요.

입력: s = "abcabcbb"

출력: 3 (정답은 "abc" 이므로 길이는 3)

입력: s = "pwwkew"

출력: 3 (정답은 "wke" 이므로 길이는 3. "pwke"는 부분 수열이지만 '연속된' 부분 문자열이 아님)
"""

import sys

s = sys.stdin.readline().strip()

left = 0

i = 0
check = set()
max_len = 0

while i < len(s):
    while s[i] in check:
        max_len = max(max_len, i-left)
        check.remove(s[left])
        left += 1

    check.add(s[i])
    i += 1

print(max(max_len,i-left)) 