def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    while i<len(s):
        m=int(s[i])
        if not m%2==0:
            m+=m
        i+=1
    return m