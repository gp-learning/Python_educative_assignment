def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    if s == "":
        return True
    elif ("{}" in s):
        return isValid(s.replace("{}", ""))
        print(s)
    elif ("[]" in s):
        return isValid(s.replace("[]", ""))
    elif ("()" in s):
        return isValid(s.replace("()", ""))
    else :
        return False

print(isValid("(as)"))