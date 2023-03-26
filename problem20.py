
def isValid( s):
    brackets = ["(", ")", "[","]","{","}"]

    if (any(bracket in s for bracket in brackets)==False):
        return True

    else:
        return False

