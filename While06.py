def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
"""
    i=0
    j=0
    new=['a','e','i','o','u','A','E','I','O','U']
    while i<len(s)+1:
        if not s[i] in new:
            j+=1
        
        i+=1
    return j
print(main("CodeschoolUz"))