def helper(s1, s2):
    if s1 == s2:
        return True
    return False

def removeWhite(s):
    excludes = (" ", ",", ".", "'", ";", ":")
    return "".join(ch.upper() for ch in s if ch not in excludes)

def isPalindrome(s):
    s = removeWhite(s)
    if len(s) <= 1:
        return True
    else:
        return helper(s[0], s[-1]) and isPalindrome(s[1:-1])


print(isPalindrome('kajak'))
print(isPalindrome('arbiter'))
