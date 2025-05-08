# Way 1
import re
def solution(s):
    return True if re.fullmatch("\d{4}|\d{6}", s) else False

# Way 2
def solution(s):
    return True if s.isdigit() and len(s) in [4, 6] else False
