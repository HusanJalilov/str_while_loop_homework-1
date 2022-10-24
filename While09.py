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
    x=0
    while i<len(s):
        m=int(s[i])
        if type(m)==int:
            x+=m
        i+=1
    return x
print(main('13'))