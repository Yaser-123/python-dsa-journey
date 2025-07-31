s = 'NITIN'
def is_palindrome(s, start, end = len(s)):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start+1, end-1)
ans = is_palindrome(s,0)
print(ans)