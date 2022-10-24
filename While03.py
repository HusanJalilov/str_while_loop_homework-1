def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    j=0
    while i<len(s):
        if not s[i].isalpha():
            j+=1
        i+=1
    return j