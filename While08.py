def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    j=0
    while i<len(s):
        m=int(s[i])
        if not m%2==0:
            j+=1
        i+=1
    return j