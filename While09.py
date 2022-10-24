def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    j=0
    while i<len(s):
        m=int(s[i])
        if m.isdigit():
            m+=m
        i+=1
    return m